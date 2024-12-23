import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")


opens = set()
start = None
end = None
for r, row in enumerate(data):
    for c, spot in enumerate(row):
        if spot == "S":
            start = (r, c)
        elif spot == "E":
            end = (r, c)
        if spot != "#":
            opens.add((r, c))

def adjacents(r, c):
    return {(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)}

def find_cheats(r, c, opens, cheat_length):
    cheats = set()
    for i in range(1, cheat_length + 1):
        for dr in range(-i, i + 1):
            for dc in range(-i, i + 1):
                if abs(dr) + abs(dc) == i and (r + dr, c + dc) in opens:
                    cheats.add((r + dr, c + dc))
    return cheats

def cheat_race(start, end, opens, cheat_length, save_threshold):
    base_steps = base_race(start, end, opens, True)
    cheats = 0
    q = [start]
    visited = {start}
    while q:
        r, c = q.pop(0)
        if (r, c) == end:
            return cheats
        for cr, cc in find_cheats(r, c, opens, cheat_length):
            cheat_time = base_steps[(r, c)] - base_steps[(cr, cc)] - distance((r, c), (cr, cc))
            if cheat_time >= save_threshold:
                cheats += 1
        for nr, nc in adjacents(r, c) & opens:
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))
    return -1

def distance(a, b):
    ar, ac = a
    br, bc = b
    return abs(br - ar) + abs(bc - ac)
        

def base_race(start, end, opens, finish_times=False):
    if finish_times:
        big_time = base_race(start, end, opens)
        visited = {start: big_time}
    else:
        visited = {start}
    q = [(*start, 0)]
    while q:
        r, c, steps = q.pop(0)
        if (r, c) == end:
            if finish_times:
                return visited
            else:
                return steps
        for nr, nc in adjacents(r, c) & opens:
            if (nr, nc) not in visited:
                if finish_times:
                    visited[(nr, nc)] = visited[(r, c)] - 1
                else:
                    visited.add((nr, nc))
                q.append((nr, nc, steps + 1))
    return -1


def solution_a():
    return cheat_race(start, end, opens, 2, 100)


def solution_b():
    return cheat_race(start, end, opens, 20, 100)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

