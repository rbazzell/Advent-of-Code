import sys
from sympy import divisors
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

#data = examples[0].input_data
data = input_data

TARGET = int(data)


def solution_a():
    for i in range(1, TARGET + 1):
        if sum(divisors(i)) * 10 >= TARGET:
            return i 

def remove_non_fifty(L: list[int], n: int):
    R = []
    for x in L:
        if x * 50 >= n:
            R.append(x)
    return R

def solution_b():
    for i in range(1, TARGET + 1):
        if sum(remove_non_fifty(divisors(i), i)) * 11 >= TARGET:
            return i 

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

