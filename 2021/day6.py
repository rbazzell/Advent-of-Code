import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

lanternfish = [data.split(",").count(str(i)) for i in range(9)]

def solution_a():
    fish = lanternfish.copy()
    days = 80
    for _ in range(days):
        fish = fish[1:] + fish[0:1]
        fish[6] += fish[8]
    return sum(fish)

def solution_b():
    fish = lanternfish.copy()
    days = 256
    for _ in range(days):
        fish = fish[1:] + fish[0:1]
        fish[6] += fish[8]
    return sum(fish)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

