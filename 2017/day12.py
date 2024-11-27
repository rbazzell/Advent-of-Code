import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
programs = {}
for line in data:
    line = line.split(" <-> ")
    programs[int(line[0])] = [int(y) for y in line[1].split(", ")]


def solution_a():
    start = 0
    visited = set()
    queue = [start]
    while queue:
        t = queue.pop(0)
        visited.add(t)
        
        for p in programs[t]:
            if p not in visited:
                queue.append(p)
    return len(visited)

def solution_b():
    groups = 0
    visited = set()
    i = 0
    queue = [i]
    while visited != len(programs): #while not full
        if not queue:
            groups += 1
            while not queue:
                i += 1
                if i >= len(programs):
                    return groups
                if i not in visited:
                    queue.append(i)
        t = queue.pop(0)
        visited.add(t)
        
        for p in programs[t]:
            if p not in visited:
                queue.append(p)
    return -1

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

