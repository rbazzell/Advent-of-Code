import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = [int(x) for x in data.split("\n")]


def solution_a():
    steps = 0
    pc = 0
    while 0 <= pc < len(data):
        data[pc] += 1
        pc += data[pc] - 1

        steps += 1
    return steps

def solution_b():
    steps = 0
    pc = 0
    while 0 <= pc < len(data):
        if data[pc] >= 3:
            data[pc] += -1
            pc += data[pc] + 1
        else:
            data[pc] += 1
            pc += data[pc] - 1

        steps += 1
    return steps

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

