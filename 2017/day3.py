import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
from math import ceil

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[1].input_data
data = input_data

data = int(data)

def solution_a():
    closest_corner = ceil(data ** 0.5)
    if closest_corner % 2 == 0:
        y = closest_corner // 2
        x = 1 - y
        dir = "RIGHT"
    else:
        x = closest_corner // 2 
        y = -x
        dir = "LEFT"
    curr = closest_corner ** 2
    while curr != data:
        curr -= 1
        match dir:
            case "UP":
                y += 1
            case "DOWN":
                y -= 1
            case "RIGHT":
                x += 1
                if x == closest_corner // 2:
                    dir = "DOWN"
            case "LEFT":
                x -= 1
                if x == -closest_corner // 2:
                    dir = "UP"
    return abs(x) + abs(y)

def solution_b():
    grid: dict[int: dict[int: int]] = {0: {0: 1}}
    x, y = 0, 0
    dir = "RIGHT"
    while grid[x][y] < data:
        match dir:
            case "UP":
                y += 1
                if y == x:
                    dir = "LEFT"
            case "DOWN":
                y -= 1
                if y == x:
                    dir = "RIGHT"
            case "RIGHT":
                x += 1
                if x == -y + 1:
                    dir = "UP"
            case "LEFT":
                x -= 1
                if x == -y:
                    dir = "DOWN"
        if not grid.get(x):
            grid[x] = dict()
        grid[x][y] = sum_adjacents(grid, x, y)
    return grid[x][y]

def sum_adjacents(grid: dict[int: dict[int: int]], x: int, y: int):
    total = 0
    for dx in [-1, 0, 1]:
        if not grid.get(x + dx):
            continue
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            if not grid[x + dx].get(y + dy):
                continue
            total += grid[x + dx][y + dy]
    return total


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

