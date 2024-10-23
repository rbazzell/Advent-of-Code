import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
data = [list(x) for x in data]


trees = [[1 if x == "#" else 0 for x in y] for y in data]

def check_slope(run, drop):
    tree_count = 0
    forest_height = len(trees)
    forest_width = len(trees[0])
    horizontal_index = 0
    for vertical_index in range(0, forest_height, drop):
        tree_count += trees[vertical_index][horizontal_index]
        horizontal_index = (horizontal_index + run) % forest_width
    return tree_count

def solution_a():
    return check_slope(3, 1)

def solution_b():
    return check_slope(1, 1) * check_slope(3, 1) * check_slope(5, 1) * check_slope(7, 1) * check_slope(1, 2)

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

