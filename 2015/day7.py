import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
print(data)


def solution_a():
    pass

def solution_b():
    pass

print(solution_a())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

