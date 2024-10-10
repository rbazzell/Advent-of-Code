import sys, copy
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

## lessons learned - When something is a solved problem (like parsing), use one of the pre-existing solutions.
#                    If you are trying to save time, it is better to use a pre-existing solution (less errors, easier to read/understand)


puzzle = aocu.get_puzzle(18, 2020)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data


data = examples[5].input_data
data = input_data

data = data.split("\n")


def eval(node):
    if isinstance(node[0], list):
        node[0] = eval(node[0])
    if isinstance(node[2], list):
        node[2] = eval(node[2])
    match node[1]:
        case "*":
            return node[0] * node[2]
        case "+":
            return node[0] + node[2]


def parse_expression(i: int, line: str) -> tuple[int, list]:
    i, curr = parse_factor(i, line)
    while i < len(line) and (line[i] == "*" or line[i] == "+"):
        oper = line[i]
        i += 1
        i, next = parse_factor(i, line)
        curr = [curr, oper, next]
    return i, curr


def parse_factor(i: int, line: str) -> tuple [int, list]:
    match line[i]:
        case "(":
            i += 1 # move past the "("
            i, curr = parse_expression(i, line)
            i += 1 # move past the ")"
        case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
            curr = int(line[i])
            i += 1 # move past the NUM
    return i, curr


def solution_a():
    trees = list()

    for line in data:
        line = line.replace(" ","")
        #tree of lists such that [a, oper, b]
        top = parse_expression(0, line)[1]
        trees.append(top)


    sum = 0
    for tree in trees:
        sum += eval(tree)
    return sum


def parse_expr(i: int, line: str) -> tuple[int, list]:
    i, curr = parse_fact(i, line)
    while i < len(line) and line[i] == "*":
        i += 1
        i, next = parse_fact(i, line)
        curr = [curr, "*", next]
    return i, curr


def parse_fact(i: int, line: str) -> tuple[int, list]:
    i, curr = parse_term(i, line)
    while i < len(line) and line[i] == "+":
        i += 1
        i, next = parse_term(i, line)
        curr = [curr, "+", next]
    return i, curr


def parse_term(i: int, line: str) -> tuple[int, list]:
    match line[i]:
        case "(":
            i += 1 # move past the "("
            i, curr = parse_expr(i, line)
            i += 1 # move past the ")"
        case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
            curr = int(line[i])
            i += 1 # move past the NUM
    return i, curr


def solution_b():
    trees = list()

    for i, line in enumerate(data):
        line = line.replace(" ", "")
        #tree of lists such that [a, oper, b]
        top = parse_expr(0, line)[1]
        trees.append(top)

    sum = 0
    for tree in trees:
        sum += eval(tree)
    return sum

print(solution_a())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

