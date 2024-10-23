import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
script = "".join(data)

def solution_a():
    x,y = 0,0
    visited = set([(x,y)])
    for direction in script:
        match direction:
            case '>':
                x += 1
            case '<':
                x -= 1
            case '^':
                y += 1
            case 'v':
                y -= 1
        visited.add((x, y))
    return len(visited)


def solution_b():
    x,y = 0,0
    rx,ry = 0,0
    visited = set([(x,y)])
    for i, direction in enumerate(script):
        if i % 2 == 0:
            match direction:
                case '>':
                    x += 1
                case '<':
                    x -= 1
                case '^':
                    y += 1
                case 'v':
                    y -= 1
            visited.add((x, y))
        else:
            match direction:
                case '>':
                    rx += 1
                case '<':
                    rx -= 1
                case '^':
                    ry += 1
                case 'v':
                    ry -= 1
            visited.add((rx, ry))
    return len(visited)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

