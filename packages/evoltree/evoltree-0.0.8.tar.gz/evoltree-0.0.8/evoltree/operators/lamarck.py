# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:29:16 2019

@author: pedro
"""
from ..algorithm.parameters import params
from ..utilities.stats.trackers import runtime_error_cache


def lamarck(ind, results, pool):
    """
    ....
    ....
    :param ind: population of individuals to be changed.
    :returns: The changed population.
    """

    if params["MULTICORE"]:
        # Add the individual to the pool of jobs.
        results.append(pool.apply_async(ind.applyLamarck, ()))
        return results
    else:
        ind2 = ind.applyLamarck()
        results.append(ind2)

    return results


def lamarck_pop(pop):
    results, pool = [], None

    if params["MULTICORE"]:
        pool = params["POOL"]

    for name, ind in enumerate(pop):
        ind.name = name
        results = lamarck(ind, results, pool)

    new_pop = []
    if params["MULTICORE"]:
        for result in results:
            # Execute all jobs in the pool.
            ind = result.get()

            # Set the fitness of the evaluated individual by placing the
            # evaluated individual back into the population.
            # pop[ind.name] = ind
            new_pop.append(ind)

            # Add the evaluated individual to the cache.
            # cache[ind.phenotype] = ind.fitness

            # Check if individual had a runtime error.
            if ind.runtime_error:
                runtime_error_cache.append(ind.phenotype)
        return new_pop
    else:
        return results


# save tree rules
def tree_to_code(tree, feature_names):
    """
    Converts a traditional decision tree to the used grammar.

    :param tree: The traditional decision tree.
    :param feature_names: The data attributes used for training.
    :return: The tree rules in the grammar's format.
    """
    from sklearn.tree import _tree

    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    # f = open(("./dt-rules.txt"), "w+")
    rules = ""

    def recurse(node, depth, rules):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            rules = rules + "np.where(x['{}'] <= {}, ".format(
                name, round(threshold, 6)
            )
            rules = recurse(tree_.children_left[node], depth + 1, rules)
            rules = rules + ", "
            rules = recurse(tree_.children_right[node], depth + 1, rules)
            rules = rules + ")"
            return rules
        else:
            prob = round(
                1
                - tree_.value[node][0][0]
                / (tree_.value[node][0][0] + tree_.value[node][0][1]),
                5,
            )
            rules = rules + "({})".format(prob)
            return rules

    rules = recurse(0, 1, rules)
    return rules
