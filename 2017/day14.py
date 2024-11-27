import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

def knot_hash(data: str):
    def xor(list: list):
        id = list[0]
        for i in range(1, len(list)):
            id ^= list[i]
        return id
    lengths = [ord(x) for x in data] + [17, 31, 73, 47, 23]
    l = [i for i in range(256)]
    c = s = 0
    for _ in range(64):
        for le in lengths:
            i = [(c + j)%len(l) for j in range(le)]
            v = [l[j] for j in i]
            for j, x in zip(i, v[::-1]):
                l[j] = x
            c = (c + le + s) % len(l)
            s += 1
    dense = [xor(l[i:i+16]) for i in range(0, len(l), 16)]
    return "".join([hex(x // 16)[-1] + hex(x % 16)[-1] for x in dense])

def solution_a():
    grid = [f"{int(knot_hash(data + f"-{i}"), 16):0>128b}" for i in range(128)]
    return sum([row.count("1") for row in grid])


def solution_b():
    grid = [f"{int(knot_hash(data + f"-{i}"), 16):0>128b}" for i in range(128)]
    for i in range(len(grid)):
        grid[i] = grid[i].replace("1", "#").replace("0", ".")
    grid = [list(row) for row in grid]
    
    queue = []
    for i in range(len(grid)-1, -1, -1):
        for j in range(len(grid[i])-1, -1, -1):
            if grid[i][j] == "#":
                queue.append((i, j))
    group = 0
    visited = set()
    while queue:
        r, c = queue.pop()

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if grid[r][c] == "#":
            group += 1
            grid[r][c] = group
            

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and (nr, nc) not in visited and grid[nr][nc] == "#":
                grid[nr][nc] = grid[r][c]
                queue.append((nr, nc))
    return group





print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

