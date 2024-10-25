import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = [list(x) for x in data.split("\n")]

def on_neighbors(grid: list[str], r:int, c:int):
    ons = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            if r + i >= len(grid) or c + j >= len(grid[r]) or r + i < 0 or c + j < 0:
                continue
            if grid[r + i][c + j] == '#':
                ons += 1
    return ons

def solution_a():
    grid = data
    new_grid = [x.copy() for x in grid]
    for step in range(100):
        for r in range(len(new_grid)):
            for c in range(len(new_grid)):
                ons = on_neighbors(grid, r, c)
                if grid[r][c] == "#" and not (ons == 2 or ons == 3):
                    new_grid[r][c] = "."
                elif grid[r][c] == "." and ons == 3:
                    new_grid[r][c] = "#"
        grid = [x.copy() for x in new_grid]
    return sum([x.count("#") for x in grid])

def solution_b():
    grid = [x.copy() for x in data]
    grid[0][0], grid[0][-1], grid[-1][0], grid [-1][-1] = ('#','#','#','#')

    new_grid = [x.copy() for x in grid]
    for step in range(100):
        for r in range(len(new_grid)):
            for c in range(len(new_grid)):
                if (r, c) in ((0, 0), (0, len(grid[r])-1), (len(grid)-1, 0), (len(grid)-1, len(grid[r])-1)):
                    new_grid[r][c] = "#"
                    continue
                ons = on_neighbors(grid, r, c)
                if grid[r][c] == "#" and not (ons == 2 or ons == 3):
                    new_grid[r][c] = "."
                elif grid[r][c] == "." and ons == 3:
                    new_grid[r][c] = "#"
        grid = [x.copy() for x in new_grid]
    return sum([x.count("#") for x in grid])

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

