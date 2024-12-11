import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
data = input_data

map = [[int(x) if x.isdigit() else -1 for x in line] for line in data.split("\n")]

def find_trail_ends(r, c):
    if map[r][c] == 9:
        return {(r, c)}
    
    trails = set()
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(map) and 0 <= nc < len(map[nr]):
            if map[nr][nc] == map[r][c] + 1:
                trails |= find_trail_ends(nr, nc)
    return trails
    
def find_trails(r, c):
    if map[r][c] == 9:
        return 1
    
    trails = 0
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(map) and 0 <= nc < len(map[nr]):
            if map[nr][nc] == map[r][c] + 1:
                trails += find_trails(nr, nc)
    return trails
    




def solution_a():
    q = []
    for r, row in enumerate(map):
        for c, tile in enumerate(row):
            if tile == 0:
                q.append((r, c))

    score = sum(len(find_trail_ends(r, c)) for r, c in q)
    return score

    


def solution_b():
    q = []
    for r, row in enumerate(map):
        for c, tile in enumerate(row):
            if tile == 0:
                q.append((r, c))

    score = sum(find_trails(r, c) for r, c in q)
    return score

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

