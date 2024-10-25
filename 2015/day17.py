import sys
import itertools
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = [int(x) for x in data.split("\n")]

LITERS = 150

def solution_a():
    solutions = []
    for l in range(1, len(data) + 1):
        for subset in itertools.combinations(data, l):
            if sum(subset) == LITERS:
                solutions.append(subset)
    return len(solutions)


def solution_b():
    solutions = []
    for l in range(1, len(data) + 1):
        for subset in itertools.combinations(data, l):
            if sum(subset) == LITERS:
                solutions.append(subset)
        if len(solutions) > 0:
            break
    return len(solutions)


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

