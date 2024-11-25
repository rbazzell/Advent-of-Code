import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[1].input_data
data = input_data

data = [[int(x) for x in line.split()] for line in data.split("\n")]

def solution_a():
    total = 0
    for line in data:
        total += max(line) - min(line)
    return total

def solution_b():
    total = 0
    for line in data:
        for i in range(len(line) - 1):
            for j in range(i+1, len(line)):
                a, b = line[i], line[j]
                if a % b == 0:
                    total += a // b
                elif b % a == 0:
                    total += b // a
    return total


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

