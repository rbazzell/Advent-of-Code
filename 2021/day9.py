import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

caves = tuple(tuple(int(x) for x in list(line)) for line in data.split("\n"))

def adjacents(r, c):
    return {(r+1, c), (r-1, c), (r, c+1), (r, c-1)}


def solution_a():
    lowests = 0
    for r, row in enumerate(caves):
        for c, spot in enumerate(row):
            lowest = True
            for nr, nc in adjacents(r, c):
                if 0 <= nr < len(caves) and 0 <= nc < len(row) and spot >= caves[nr][nc]:
                    lowest = False
            if lowest:
                lowests += spot + 1
    return lowests

def solution_b():
    basins = []
    visited = set()
    for R, row in enumerate(caves):
        for C, spot in enumerate(row):
            if (R, C) not in visited and spot != 9:
                q = [(R, C)]
                basin = 0
                while q:
                    r, c = q.pop(0)
                    if (r, c) not in visited:
                        visited.add((r, c))
                        basin += 1

                        for nr, nc in adjacents(r, c):
                            if 0 <= nr < len(caves) and 0 <= nc < len(row) and (nr, nc) not in visited and caves[nr][nc] != 9:
                                q.append((nr, nc))
                basins.append(basin)
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]
                            

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

