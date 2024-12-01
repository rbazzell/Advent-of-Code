import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
left = [int(line.split()[0]) for line in data]
right = [int(line.split()[1]) for line in data]
counts = [right.count(l) for l in left]


def solution_a():
    left.sort()
    right.sort()
    return sum(abs(l - r) for l, r in zip(left, right))


def solution_b():
    return sum(l*r for l, r in zip(left, counts))

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

