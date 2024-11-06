import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

discs = {}
for i in range(len(data)):
    line = data[i].split(" ")
    positions = int(line[3])
    start_position = int(line[-1][:-1])
    discs[i + 1] = (positions, start_position)

def product(iterable):
    product = 1
    for item in iterable:
        product *= item
    return product


def solution_a():
    for t in range(product(info[0] for info in discs.values())):
        for d, info in discs.items():
            p, s = info
            found = True
            if (t + d + s) % p != 0:
                found = False
                break
        if found:
            return t
    return -1


def solution_b():
    discs[i + 2] = (11, 0)
    for t in range(product(info[0] for info in discs.values())):
        for d, info in discs.items():
            p, s = info
            found = True
            if (t + d + s) % p != 0:
                found = False
                break
        if found:
            return t
    return -1

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

