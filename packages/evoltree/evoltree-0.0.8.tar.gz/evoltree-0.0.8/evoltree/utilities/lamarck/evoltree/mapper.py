from ...utils import roundAllNums
import random

# Build the lexer


def getval(n):
    # if n not in ts: print(f"Undefined name '{n}'")
    return ts.get(n, 0)


def p_error(t):
    # print(f"Syntax error at '{t.value}', [{t.lexer.lineno}]")
    pass


def get_genome_from_dt_idf(phenotype):
    phenotype = roundAllNums(phenotype)
    return parser.parse(phenotype)


literals = "+-/*=().[],<>"
t_ignore = " \t\n'\""

t_npwhere = "np.where"
t_x = "x"


def t_NUMBER(t):
    r"\d"
    t.value = int(t.value)
    return t


def t_error(t):
    # print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
    t.lexer.skip(1)


def gen_rnd(chosen, productions):
    factor = 255 // productions
    return random.randint(0, factor) * productions + chosen


# symboltable : dictionary of names
ts = {}
# Grammar
def p_1(t):
    "result : npwhere '(' x '[' idx ']' comparison value ',' node ',' node ')'"
    t[0] = [gen_rnd(0, 1)] + t[5] + t[7] + t[8] + t[10] + t[12]


def p_2(t):
    "node : result"
    t[0] = [gen_rnd(0, 2)] + t[1]


def p_3(t):
    "node : '(' leaf ')'"
    t[0] = [gen_rnd(1, 2)] + t[2]


def p_4(t):
    "leaf : NUMBER '.' digits"
    t[0] = [gen_rnd(0, 2)] + t[3]


def p_5(t):
    "leaf : NUMBER"
    t[0] = [gen_rnd(1, 2)]


def p_6(t):
    "digits : digits digit"
    t[0] = [gen_rnd(0, 2)] + t[1] + t[2]


def p_7(t):
    "digits : digit"
    t[0] = [gen_rnd(1, 2)] + t[1]


def p_8(t):
    "digit : NUMBER"
    t[0] = [gen_rnd(t[1], 10)]


def p_9(t):
    "comparison : '=' '='"
    t[0] = [gen_rnd(0, 4)]


def p_10(t):
    "comparison : '<'"
    t[0] = [gen_rnd(1, 4)]


def p_11(t):
    "comparison : '>'"
    t[0] = [gen_rnd(2, 4)]


def p_12(t):
    "comparison : '<' '='"
    t[0] = [gen_rnd(3, 4)]


def p_13(t):
    "value : digits '.' digits"
    t[0] = [gen_rnd(0, 2)] + t[1] + t[3]


def p_14(t):
    "value : digits"
    t[0] = [gen_rnd(1, 2)] + t[1]

def p_15(t) : "idx : col1" ; t[0] = [gen_rnd(0, 10)]
def p_16(t) : "idx : col2" ; t[0] = [gen_rnd(1, 10)]
def p_17(t) : "idx : col3" ; t[0] = [gen_rnd(2, 10)]
def p_18(t) : "idx : col4" ; t[0] = [gen_rnd(3, 10)]
def p_19(t) : "idx : col5" ; t[0] = [gen_rnd(4, 10)]
def p_20(t) : "idx : col6" ; t[0] = [gen_rnd(5, 10)]
def p_21(t) : "idx : col7" ; t[0] = [gen_rnd(6, 10)]
def p_22(t) : "idx : col8" ; t[0] = [gen_rnd(7, 10)]
def p_23(t) : "idx : col9" ; t[0] = [gen_rnd(8, 10)]
def p_24(t) : "idx : col10" ; t[0] = [gen_rnd(9, 10)]

tokens = ('NUMBER', 'npwhere', 'x', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10',)

t_col1 = "col1"
t_col2 = "col2"
t_col3 = "col3"
t_col4 = "col4"
t_col5 = "col5"
t_col6 = "col6"
t_col7 = "col7"
t_col8 = "col8"
t_col9 = "col9"
t_col10 = "col10"

from ply.lex import lex
from ply.yacc import yacc
lexer = lex()
parser = yacc(debug=False)
