import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

map: list[str] = data.split("\n")
digits: dict[int, tuple[int, int]] = dict()
for r, row in enumerate(map):
    for c, char in enumerate(row):
        if char.isdigit():
            digits[int(char)] = (r, c)


def shortest_distances():
    #first find the shortest distance between every digit and every other digit (BFS):
    shortest_distances: dict[int, dict[int, int]] = dict()
    for digit, coord in digits.items():
        S = shortest_distances[digit] = dict()
        r, c = coord
        queue = [(r, c, 0)]
        visited = set()

        for d, weights in shortest_distances.items():
            if weights.get(digit):
                S[d] = weights.get(digit)


        while len(S) < len(digits) and queue:
            r, c, steps = queue.pop(0)
            
            tile = map[r][c]
            if tile.isdigit() and S.get(tile) == None:
                S[int(tile)] = steps

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited and map[nr][nc] != "#":
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))
    return shortest_distances


def solution_a():
    S = shortest_distances()
    #then find the smallest combination of paths for this (BFS)
    min_steps = 999999999999999
    queue = [(0, 0, {0})] #node, steps, path
    while queue:
        node, steps, path = queue.pop(0)
        if len(path) == len(digits):
            min_steps = min(min_steps, steps)
        
        for dest, s in S[node].items():
            if dest not in path:
                queue.append((dest, steps + s, path | {dest}))
    return min_steps

def solution_b():
    S = shortest_distances()
    #then find the smallest combination of paths for this (BFS)
    min_steps = 999999999999999
    queue = [(0, 0, {0})] #node, steps, path
    while queue:
        node, steps, path = queue.pop(0)
        if len(path) == len(digits):
            min_steps = min(min_steps, steps + S[node][0])
        
        for dest, s in S[node].items():
            if dest not in path:
                queue.append((dest, steps + s, path | {dest}))
    return min_steps

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

