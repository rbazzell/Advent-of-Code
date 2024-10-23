import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[7].input_data
data = input_data

data = data.split("\n")


def solution_a():
    floor = 0
    for line in data:
        for paren in line:
            floor += (1 if paren == '(' else -1)
    return floor

def solution_b():
    floor = 0
    i = 0
    for line in data:
        for paren in line:
            i += 1
            floor += (1 if paren == '(' else -1)
            if floor < 0:
                return i

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

