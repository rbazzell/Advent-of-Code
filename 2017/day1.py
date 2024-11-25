import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[8].input_data
data = input_data

data = [int(x) for x in data]


def solution_a():
    total = data[-1] if data[-1] == data[0] else 0
    for i in range(len(data) - 1):
        if data[i] == data[i+1]:
            total += data[i]
    return total


def solution_b():
    total = 0
    for i in range(len(data)//2):
        if data[i] == data[len(data)//2 + i]:
            total += 2 * data[i]
    return total

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

