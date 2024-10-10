import sys, copy
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
from misc.aoc_utilities import print_grid

puzzle = aocu.get_puzzle(11, 2020)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

data = [list(x) for x in data]


def solution_a():
    prev = 0
    curr = copy.deepcopy(data)

    while not prev == curr:
        prev = copy.deepcopy(curr)
        for row in range(len(curr)):
            for col in range(len(curr[row])):
                adj_occupied = adjacent('#', row, col, prev)
                if prev[row][col] == 'L' and adj_occupied == 0:
                    curr[row][col] = '#'
                elif prev[row][col] == '#' and adj_occupied >= 4:
                    curr[row][col] = 'L'
    
    occupied_seats = 0
    for x in curr:
        for y in x:
            if y == '#':
                occupied_seats += 1
    return occupied_seats


def adjacent(type_to_check, row, col, grid):
    total = 0
    for i in [-1, 0, 1]:
        if (row + i) >= len(grid) or (row + i) < 0:
            continue
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            if (col + j) >= len(grid[row + i]) or (col + j) < 0:
                continue
            if grid[row + i][col + j] == type_to_check:
                total += 1
    return total

def line_of_sight(type_to_check, row, col, grid):
    total = 0
    for r in [-1, 0, 1]:
        if (row + r) >= len(grid) or (row + r) < 0:
            continue
        for c in [-1, 0, 1]:
            if r == 0 and c == 0:
                continue
            if (col + c) >= len(grid[row + r]) or (col + c) < 0:
                continue
            mr, mc = 0, 0
            while True:
                mr += r
                mc += c
                if (row + mr) >= len(grid) or (row + mr) < 0:
                    break
                if (col + mc) >= len(grid[row + mr]) or (col + mc) < 0:
                    break
                if grid[row + mr][col + mc] != '.':
                    total += 1 if grid[row + mr][col + mc] == type_to_check else 0
                    break
    return total

def solution_b():
    prev = 0
    curr = copy.deepcopy(data)

    while not prev == curr:
        prev = copy.deepcopy(curr)
        for row in range(len(curr)):
            for col in range(len(curr[row])):
                los_occupied = line_of_sight('#', row, col, prev)
                if prev[row][col] == 'L' and los_occupied == 0:
                    curr[row][col] = '#'
                elif prev[row][col] == '#' and los_occupied >= 5:
                    curr[row][col] = 'L'
    
    occupied_seats = 0
    for x in curr:
        for y in x:
            if y == '#':
                occupied_seats += 1
    return occupied_seats

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

