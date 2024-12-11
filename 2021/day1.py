import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

sonar = [int(x) for x in data.split("\n")]

def solution_a():
    increases = 0
    for i in range(1, len(sonar)):
        if sonar[i] > sonar[i - 1]:
            increases += 1
    return increases


def solution_b():
    increases = 0
    for i in range(3, len(sonar)):
        if sum(sonar[i-2:i+1]) > sum(sonar[i-3:i]):
            increases += 1
    return increases

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

