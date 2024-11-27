import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
#data = input_data

steps = int(data)


def solution_a():
    spinlock = [0]
    i = 0
    for v in range(1, 2018):
        i =  (i + steps) % len(spinlock) + 1
        spinlock = spinlock[:i] + [v] + spinlock[i:]
    return spinlock[spinlock.index(2017)+1]


def solution_b():
    spinlock = None
    i = 0
    # The author of AoC said 50 billion was probably too large a loop - lol
    # it takes ~5 seconds to compute, even with this very efficient method
    # 1 billion probably would have been more appropriate
    for v in range(1, 50000001):
        i = (i + steps) % (v) + 1
        if i == 1:
            spinlock = v
    return spinlock
print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

