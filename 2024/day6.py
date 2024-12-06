import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

lab = [list(line) for line in data.split("\n")]

for r, row in enumerate(lab):
    for c, space in enumerate(row):
        if space not in (".", "#"):
            start = r, c, space

def move(r, c, dir):
    dr, dc = {"^": (-1, 0), ">": (0, 1), "V": (1, 0), "<": (0, -1)}[dir]
    return r + dr, c + dc

def rotate(dir):
    return {"^": ">", ">": "V", "V": "<", "<": "^"}[dir]



def solution_a():
    walked = set()
    r, c, dir = start
    while 0 <= r < len(lab) and 0 <= c < len(lab[r]):
        walked.add((r, c))
        nr, nc = move(r, c, dir)
        if 0 <= nr < len(lab) and 0 <= nc < len(lab[r]) and lab[nr][nc] == "#":
            dir = rotate(dir)
            nr, nc = move(r, c, dir)
        r, c = nr, nc
    return len(walked)


def solution_b():
    walked = set()
    r, c, dir = start
    while 0 <= r < len(lab) and 0 <= c < len(lab[r]):
        walked.add((r, c))
        nr, nc = move(r, c, dir)
        if 0 <= nr < len(lab) and 0 <= nc < len(lab[r]) and lab[nr][nc] == "#":
            dir = rotate(dir)
            nr, nc = move(r, c, dir)
        r, c = nr, nc
        
    loops = 0
    for point in walked - {start[:2]}:
        visited = set()
        r, c, dir = start
        while 0 <= r < len(lab) and 0 <= c < len(lab[r]) and (r, c, dir) not in visited:
            visited.add((r, c, dir))
            nr, nc = move(r, c, dir)
            #                    in bounds                  and                  obstacle
            if 0 <= nr < len(lab) and 0 <= nc < len(lab[r]) and (lab[nr][nc] == "#" or (nr, nc) == point):
                dir = rotate(dir)
            else:
                r, c = nr, nc
        if (r, c, dir) in visited:
            loops += 1
    return loops

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

