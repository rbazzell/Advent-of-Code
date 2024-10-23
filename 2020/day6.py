import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[1].input_data
data = input_data

data = data.split("\n\n")
any_yes = [set(x) - set("\n") for x in data]
data = [[set(y)for y in x.split()] for x in data]

def solution_a():
    yeses = 0
    for group in any_yes:
        yeses += len(group)
    return yeses

def solution_b():
    yeses = 0
    for group in data:
        group_set = group[0]
        for person in group:
            group_set = group_set.intersection(person)
        yeses += len(group_set)
    return yeses
        

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

