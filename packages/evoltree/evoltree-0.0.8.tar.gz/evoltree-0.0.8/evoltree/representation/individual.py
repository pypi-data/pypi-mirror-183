import numpy as np
import random
import re
import math
from importlib import import_module
from sklearn.tree import DecisionTreeClassifier

from ..algorithm.mapper import map_tree_from_genome
from ..operators.lamarck import tree_to_code
from ..algorithm.mapper import mapper
from ..algorithm.parameters import params
from ..utilities.fitness.get_data import get_data, get_data_sample
from ..utilities.algorithm.NSGA2 import dominates


class Individual(object):
    """
    A GE individual.
    """

    def __init__(self, genome, ind_tree, map_ind=True):
        """
        Initialise an instance of the individual class (i.e. create a new
        individual).

        :param genome: An individual's genome.
        :param ind_tree: An individual's derivation tree, i.e. an instance
        of the representation.tree.Tree class.
        :param map_ind: A boolean flag that indicates whether or not an
        individual needs to be mapped.
        """

        if map_ind:
            # The individual needs to be mapped from the given input
            # parameters.
            (
                self.phenotype,
                self.genome,
                self.tree,
                self.nodes,
                self.invalid,
                self.depth,
                self.used_codons,
            ) = mapper(genome, ind_tree)

        else:
            # The individual does not need to be mapped.
            self.genome, self.tree = genome, ind_tree

        self.fitness = params["FITNESS_FUNCTION"].default_fitness
        self.runtime_error = False
        self.name = None

    def __lt__(self, other):
        """
        Set the definition for comparison of two instances of the individual
        class by their fitness values. Allows for sorting/ordering of a
        population of individuals. Note that numpy NaN is used for invalid
        individuals and is used by some fitness functions as a default fitness.
        We implement a custom catch for these NaN values.

        :param other: Another instance of the individual class (i.e. another
        individual) with which to compare.
        :return: Whether or not the fitness of the current individual is
        greater than the comparison individual.
        """

        if np.isnan(self.fitness):
            return True
        elif np.isnan(other.fitness):
            return False
        else:
            return (
                self.fitness < other.fitness
                if params["FITNESS_FUNCTION"].maximise
                else other.fitness < self.fitness
            )

    def __le__(self, other):
        """
        Set the definition for comparison of two instances of the individual
        class by their fitness values. Allows for sorting/ordering of a
        population of individuals. Note that numpy NaN is used for invalid
        individuals and is used by some fitness functions as a default fitness.
        We implement a custom catch for these NaN values.

        :param other: Another instance of the individual class (i.e. another
        individual) with which to compare.
        :return: Whether or not the fitness of the current individual is
        greater than or equal to the comparison individual.
        """

        if np.isnan(self.fitness):
            return True
        elif np.isnan(other.fitness):
            return False
        else:
            return (
                self.fitness <= other.fitness
                if params["FITNESS_FUNCTION"].maximise
                else other.fitness <= self.fitness
            )

    def __str__(self):
        """
        Generates a string by which individuals can be identified. Useful
        for printing information about individuals.

        :return: A string describing the individual.
        """
        return (
            "Individual: "
            + str(self.phenotype)
            + "; "
            + str(self.fitness)
            + ";"
            + str(self.genome)
        )

    def deep_copy(self):
        """
        Copy an individual and return a unique version of that individual.

        :return: A unique copy of the individual.
        """

        if not params["GENOME_OPERATIONS"]:
            # Create a new unique copy of the tree.
            new_tree = self.tree.__copy__()

        else:
            new_tree = None

        # Create a copy of self by initialising a new individual.
        new_ind = Individual(self.genome.copy(), new_tree, map_ind=False)

        # Set new individual parameters (no need to map genome to new
        # individual).
        new_ind.phenotype, new_ind.invalid = self.phenotype, self.invalid
        new_ind.depth, new_ind.nodes = self.depth, self.nodes
        new_ind.used_codons = self.used_codons
        new_ind.runtime_error = self.runtime_error

        return new_ind

    def evaluate(self):
        """
        Evaluates phenotype in using the fitness function set in the params
        dictionary. For regression/classification problems, allows for
        evaluation on either training or test distributions. Sets fitness
        value.

        :return: Nothing unless multicore evaluation is being used. In that
        case, returns self.
        """
        # Evaluate fitness using specified fitness function.
        if params["OPTIMIZE_CONSTANTS"]:
            from utilities.fitness.optimize_constants import optimize_constants
            from utilities.utils import remove_leading_zeros

            self.phenotype = remove_leading_zeros(self.phenotype)
            # if we are training, then optimize the constants by
            # gradient descent and save the resulting phenotype
            # string as ind.phenotype_with_c0123 (eg x[0] +
            # c[0] * x[1]**c[1]) and values for constants as
            # ind.opt_consts (eg (0.5, 0.7). Later, when testing,
            # use the saved string and constants to evaluate.
            _, ind = optimize_constants(
                params["X_train"], params["y_train"], self
            )
            if ind is not None:
                self = ind.deep_copy()

        self.fitness = params["FITNESS_FUNCTION"](self)

        if params["MULTICORE"]:
            return self

    def applyLamarck(self):
        """
        Applies Lamarck to individual. It consists in select a random node,
        train a traditional Decision Tree with data that fall in that node,
        replace that node with the trained DT, evaluate the individual and
        replace it if the fitness improves.
        :param ind: an individual to be changed.
        :returns: The changed individual.
        """
        if random.random() < params["LAMARCK_PROBABILITY"]:
            x, y, _, _ = get_data(
                params["DATASET_TRAIN"], params["DATASET_TEST"]
            )
            ind = self.deep_copy()
            phenotype = ind.phenotype
            # Check number of nodes (np.where)
            nrNodes = phenotype.count("np.where")
            # Expressions with root node only, are replaced by a traditional dt
            if nrNodes == 1:
                dt = self.__get_traditional_tree(x, y, max_depth=5)
                # get the tree rules
                try:  ### NEW 16-11-2020
                    rules = tree_to_code(dt, x.columns.tolist() + ["target"])
                except:  # decision tree is too small, generates error
                    return self
                ind.phenotype = rules
                ind.evaluate()
                if dominates(ind, self):
                    fitness = ind.fitness
                    ind = self.__update_individual(ind, rules)
                    ind.fitness = fitness
                    return ind
                else:
                    return self

            else:
                newExp, startPos, endPos = self.__get_subtree(
                    phenotype, nrNodes
                )
                # if params["N_SAMPLING"] > 0:
                #    x, y = get_data_sample(params["N_SAMPLING"])
                # index of records that fall on the changed expression
                index = np.where(eval(newExp) == 100)[0]
                if len(index) > 0:
                    X2 = x.iloc[index, :]
                    y2 = y.iloc[index]
                    # train a traditional decision tree using only the data that falls in the subtree
                    dt = self.__get_traditional_tree(X2, y2, max_depth=5)
                    # get the tree rules
                    try:  ### NEW 16-11-2020
                        rules = tree_to_code(
                            dt, x.columns.tolist() + ["target"]
                        )
                    except:  # decision tree is too small, generates error
                        return self
                    # add the rules to the old phenotype
                    newPhenotype = (
                        phenotype[0:startPos]
                        + rules
                        + phenotype[(startPos + endPos + 1) :]
                    )

                    ind.phenotype = newPhenotype
                    ind.evaluate()
                    if dominates(ind, self):
                        fitness = ind.fitness
                        ind = self.__update_individual(ind, newPhenotype)
                        ind.fitness = fitness
                        return ind
                    else:
                        return self

                else:
                    # NEW: 21/11/2022
                    # If no data fals in this node, let's replace it by 0.5 (tree prunning)
                    # AUC will be the same, but the tree is smaller :)
                    # TODO: if grammar changes (which is my next idea), this won't work :(
                    newPhenotype = (
                        phenotype[0:startPos]
                        + "(0.5)"
                        + phenotype[(startPos + endPos + 1) :]
                    )
                    ind = self.__update_individual(ind, newPhenotype)
                    if params["N_SAMPLING"] > 0:
                        x, y = get_data_sample(params["N_SAMPLING"])
                    ind.evaluate()
                    return ind

        else:
            return self

    ### NEW 02-01-2021
    def predict(self, x):
        return eval(self.phenotype)

    # NEW 21/11/2022: clean the code using auxiliary functions
    def __get_traditional_tree(self, X, y, **kwargs) -> DecisionTreeClassifier:
        return DecisionTreeClassifier(
            random_state=params["RANDOM_SEED"], **kwargs
        ).fit(X, y)

    def __update_individual(self, ind, phenotype):
        i = import_module(params["LAMARCK_MAPPER"])
        ind.phenotype = phenotype
        # print(phenotype)

        try:
            genome = i.get_genome_from_dt_idf(phenotype)
            ind.genome = genome
            mapped = map_tree_from_genome(genome)
            ind.tree = mapped[2]
            ind.nodes = mapped[3]
            return ind
        except Exception as e:
            # print(f"exception: {e} \n Phenotype: {phenotype} \n Genome: {genome}")
            return self

    def __get_subtree(self, phenotype, nrNodes):
        """
        Get a random subtree to be replaced by a traditional decision tree.

        Gets a random subtree (sub-expression) from the original phenotype, and
        its start and end indexes in the original phenotype.
        This subtree (expression) will be further replaced by a traditional DT (rules).

        Parameters
        ----------
        phenotype : _type_
            Original phenotype (Evolutionary Decision Tree).
        nrNodes : _type_
            Number of nodes/decisions (subtrees).

        Returns
        -------
        Tuple
            Returns the subtree and its start and end indexes in the original phenotype.
        """
        # select a random node (can't be the first)
        randNode = random.randint(
            0, nrNodes - 1
        )  # -1 due to the index starting at 0
        # get all nodes' positions
        allNodes = [node.start() for node in re.finditer("np.where", phenotype)]
        # get node position
        nodePosition = allNodes[randNode]
        # get the expression
        #   get opened and closed brackets' positions
        openBrPos = [
            m.start() for m in re.finditer("\(", phenotype[nodePosition:])
        ]
        closeBrPos = [
            m.start() for m in re.finditer("\)", phenotype[nodePosition:])
        ]
        allBrPos = sorted(openBrPos + closeBrPos)
        # get the position where the expression to be replaced ends
        openBr = 0
        closeBr = 0
        position = 1
        for i in range(0, len(allBrPos)):
            pos = allBrPos[i]
            if pos in openBrPos:
                openBr = openBr + 1
            elif pos in closeBrPos:
                closeBr = closeBr + 1
            if openBr == closeBr:
                position = pos
                break
        # expression to be replaced:
        replaceExp = phenotype[nodePosition : (position + nodePosition + 1)]
        #   subtree leafs, to identify records that fall there
        toReplace = re.findall(
            "\([-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?\)",
            replaceExp,
        )
        for val in toReplace:
            replaceExp = replaceExp.replace(val, "100")
        # new expression with this values
        newExp = (
            phenotype[0:nodePosition]
            + replaceExp
            + phenotype[(position + nodePosition + 1) :]
        )

        return newExp, nodePosition, position
