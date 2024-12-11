import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

lines = tuple(tuple(tuple(int(x) for x in point.split(",")) for point in line.split(" -> ")) for line in data.split("\n"))

def solution_a():
    vents = dict()
    for a, b in lines:
        ax, ay = a
        bx, by = b
        if ax == bx:
            x = ax
            for y in range(min(ay, by), max(ay, by) + 1):
                if (x, y) not in vents:
                    vents[(x, y)] = 0
                vents[(x, y)] += 1
        elif ay == by:
            y = ay
            for x in range(min(ax, bx), max(ax, bx) + 1):
                if (x, y) not in vents:
                    vents[(x, y)] = 0
                vents[(x, y)] += 1
    vent_count = 0
    for vent in vents.values():
        if vent > 1:
            vent_count += 1
    return vent_count


def solution_b():
    vents = dict()
    for a, b in lines:
        ax, ay = a
        bx, by = b
        if ax == bx:
            x = ax
            for y in range(min(ay, by), max(ay, by) + 1):
                if (x, y) not in vents:
                    vents[(x, y)] = 0
                vents[(x, y)] += 1
        elif ay == by:
            y = ay
            for x in range(min(ax, bx), max(ax, bx) + 1):
                if (x, y) not in vents:
                    vents[(x, y)] = 0
                vents[(x, y)] += 1
        else:
            step = -1 if ax-bx != ay-by else 1
            bot = {1: min,
                   -1: max}
            top = {1: max,
                   -1: min}
            for x, y in zip(range(min(ax, bx), max(ax, bx) + 1), range(bot[step](ay, by), top[step](ay, by) + step, step)):
                if (x, y) not in vents:
                    vents[(x, y)] = 0
                vents[(x, y)] += 1

    vent_count = 0
    for vent in vents.values():
        if vent > 1:
            vent_count += 1
    return vent_count

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

