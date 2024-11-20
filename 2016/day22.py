import sys
from dataclasses import dataclass
from copy import deepcopy
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = "root@ebhq-gridcenter# df -h\n" + examples[0].input_data
data = input_data

data = data.split("\n")

@dataclass
class Node:
    size: int
    used: int
    avail: int
    usep: int


grid: dict[int, dict[int, Node]] = {}
for line in data[2:]:
    line = line.split()
    x, y = (int(a[1:]) for a in line[0].split("-")[1:])
    node = Node(*(int(a[:-1]) for a in line[1:]))
    if not grid.get(x):
        grid[x] = dict()
    grid[x][y] = node

def solution_a(submit=True):
    viable_pairs = set()
    empty = None
    for Ax in range(len(grid)):
        for Ay in range(len(grid[Ax])):
            for Bx in range(len(grid)):
                for By in range(len(grid[Bx])):
                    if Bx == Ax and By == Ay:
                        continue
                    A, B = grid[Ax][Ay], grid[Bx][By]
                    if A.used and A.used <= B.avail:
                        viable_pairs.add((Ax, Ay))
                        empty = (Bx, By)
    
    return len(viable_pairs) if submit else (viable_pairs, empty)
                    

def find_path_for_goal(viable: set[tuple[int, int]]) -> list[tuple[int, int]]:
    x, y = len(grid) - 1, 0
    queue = [(x, y, [(x, y)])]
    visited: set[tuple[int, int]] = set()

    while queue:
        x, y, path = queue.pop(0)  
        #reached endpoint
        if x == 0 and y == 0:
            return path

        #not a viable point
        if (x, y) not in viable:
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            #out of bounds
            if x + dx >= len(grid) or x + dx < 0 or y + dy >= len(grid[x]) or y + dy < 0:
                continue
            if (x + dx, y + dy) not in visited:
                visited.add((x + dx, y + dy))
                queue.append((x + dx, y + dy, path + [(x + dx, y + dy)]))
    return []

def solution_b(): #more BFS - yay...
    viable, empty = solution_a(False)
    path = find_path_for_goal(viable)

    steps = 0
    ogx, ogy = empty
    gx, gy = path.pop(0)
    while path:
        x, y = ogx, ogy
        ogx, ogy = gx, gy
        gx, gy = path.pop(0) #g stands for goal
        queue = [(x, y, steps)]
        visited: set[tuple[int, int]] = set()
        V = (viable | {(gx, gy), empty}) - {(ogx, ogy)}

        while queue:
            x, y, steps = queue.pop(0)
            if x == gx and y == gy:
                steps += 1
                break

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                #out of bounds
                if x + dx >= len(grid) or x + dx < 0 or y + dy >= len(grid[x]) or y + dy < 0:
                    continue
                if (x + dx, y + dy) in V:
                    queue.append((x + dx, y + dy, steps + 1))
    return steps


            




        


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

