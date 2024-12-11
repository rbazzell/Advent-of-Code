import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

crabs = sorted(int(x) for x in data.split(","))

def solution_a():
    x = (crabs[len(crabs)//2] + crabs[len(crabs)//2 - 1]) // 2 #median minimizes total abs difference
    fuel = 0
    for crab in crabs:
        fuel += abs(x - crab)
    return fuel


def solution_b():
    x = sum(crabs)//len(crabs) # find average, which minimizes difference squared
    min_fuel = 99999999999
    for y in range(x - 5, x + 6): # test values around mean, since it's not a raw square
        fuel = 0
        for crab in crabs:
            fuel += ((y - crab) ** 2 + abs(y - crab)) // 2 # triangle number calculation
        min_fuel = min(min_fuel, fuel)
    return min_fuel

    

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

