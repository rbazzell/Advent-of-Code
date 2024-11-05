import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data, target = examples[0].input_data, (7, 4)
data, target = input_data, (31, 39)

fav_num = int(data)

grid = {}

def neighbors(p: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = p
    neighbors = []
    for x_, y_ in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
        p_ = (x_, y_)
        if x_ < 0 or y_ < 0:
            continue
        elif p_ not in grid.keys():
            grid[p_] = '#' if num_of_1_bits(x_*x_ + 3*x_ + 2*x_*y_ + y_ + y_*y_ + fav_num) & 1 else '.'
        
        if grid[p_] == '.':
            neighbors.append(p_)
    return neighbors
        


def num_of_1_bits(num: int) -> int:
    sum = 0
    while num > 0:
        sum += num & 1
        num >>= 1
    return sum

def solution_a():
    curr = (1, 1)
    queue = [(curr, 0)]
    grid[curr] = '.'
    visited = {curr}
    while queue:
        point, step = queue.pop(0)
        if point == target:
            return step
        for neighbor in neighbors(point):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, step + 1))
    return -1

def solution_b():
    curr = (1, 1)
    queue = [(curr, 0)]
    grid[curr] = '.'
    visited = {curr}
    fifty = 0
    while queue:
        point, step = queue.pop(0)
        if step <= 50:
            fifty += 1
        else:
            return fifty
        for neighbor in neighbors(point):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, step + 1))
    return -1

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

