import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

grid = [list(line) for line in data.split("\n")]


antenna: dict[str, list[tuple[int, int]]] = dict()
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell != ".":
            if cell not in antenna:
                antenna[cell] = list()
            antenna[cell].append((r, c))



def solution_a():
    antinodes = set()
    for locations in antenna.values():
        locations.sort(key=lambda x: (x[0], x[1]))
        for i, a in enumerate(locations):
            for b in locations[i+1:]:
                rise, run = b[0] - a[0], b[1] - a[1]
                if 0 <= a[0]-rise < len(grid) and 0 <= a[1]-run < len(grid[0]):
                    antinodes.add((a[0]-rise, a[1]-run))
                if 0 <= b[0]+rise < len(grid) and 0 <= b[1]+run < len(grid[0]):
                    antinodes.add((b[0]+rise, b[1]+run))
    return len(antinodes)


def solution_b():
    antinodes = set()
    for locations in antenna.values():
        locations.sort(key=lambda x: (x[0], x[1]))
        for i, ao in enumerate(locations):
            for b in locations[i+1:]:
                a = ao
                rise, run = b[0] - a[0], b[1] - a[1]
                while 0 <= a[0] < len(grid) and 0 <= a[1] < len(grid[0]):
                    antinodes.add(a)
                    a = (a[0]-rise, a[1]-run)
                while 0 <= b[0] < len(grid) and 0 <= b[1] < len(grid[0]):
                    antinodes.add(b)
                    b = (b[0]+rise, b[1]+run)
    return len(antinodes)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

