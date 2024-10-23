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

start = set()

for x, r in enumerate(data):
    for y, c in enumerate(r):
        if c == "#":
            start.add((x, y, 0))

def neighbors3d(point: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    x, y, z = point
    ns = set()
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if i == 0 and j == 0 and k == 0:
                    continue
                ns.add((x + i, y + j, z + k))
    return ns

def neighbors4d(point: tuple[int, int, int, int]) -> set[tuple[int, int, int, int]]:
    x, y, z, w = point
    ns = set()
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue
                    ns.add((x + i, y + j, z + k, w + l))
    return ns

def solution_a():
    active = start.copy()
    for i in range(6):
        old_active = active.copy()
        old_inactive = set()
        for p in old_active:
            old_inactive.update(neighbors3d(p) - old_active)
        
        active.clear()
        for p in old_active:
            active_neighbors = sum([1 for n in neighbors3d(p) if n in old_active])
            if active_neighbors == 2 or active_neighbors == 3:
                active.add(p)

        for p in old_inactive:
            active_neighbors = sum([1 for n in neighbors3d(p) if n in old_active])
            if active_neighbors == 3:
                active.add(p)
    return len(active)

def solution_b():
    active = fourthify(start)
    for i in range(6):
        old_active = active.copy()
        old_inactive = set()
        for p in old_active:
            old_inactive.update(neighbors4d(p) - old_active)
        
        active.clear()
        for p in old_active:
            active_neighbors = sum([1 for n in neighbors4d(p) if n in old_active])
            if active_neighbors == 2 or active_neighbors == 3:
                active.add(p)

        for p in old_inactive:
            active_neighbors = sum([1 for n in neighbors4d(p) if n in old_active])
            if active_neighbors == 3:
                active.add(p)
    return len(active)

def fourthify(a: set[tuple[int, int, int]]) -> set[tuple[int, int, int, int]]:
    f = set()
    for x, y, z, in a:
        f.add((x, y, z, 0))
    return f

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

