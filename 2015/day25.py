import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = "row: 5, column 6."
data = input_data


row = int(data.split(" ")[-3][:-1])
col = int(data.split(" ")[-1][:-1])

def solution_a():
    n = (row + col - 1)
    iters = (n * (n + 1) // 2) - row
    code = 20151125
    for iter in range(iters):
        code = (code * 252533) % 33554393
    return code

def solution_b():
    pass

print(solution_a())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

