import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

map = {}

for y, line in enumerate(data.split("\n")):
    for x, c in enumerate(line):
        if x not in map:
            map[x] = dict()
        map[x][y] = c

def solution_a():
    infections = 0
    dir = "U"
    x, y = len(map) // 2, len(map) // 2
    for _ in range(10000):
        if x not in map:
            map[x] = dict()
        if y not in map[x] or map[x][y] == ".":
            match dir:
                case "U":
                    dir = "L"
                case "D":
                    dir = "R"
                case "R":
                    dir = "U"
                case "L":
                    dir = "D"
            map[x][y] = "#"
            infections += 1
        else:
            match dir:
                case "U":
                    dir = "R"
                case "D":
                    dir = "L"
                case "R":
                    dir = "D"
                case "L":
                    dir = "U"
            map[x][y] = "."
        match dir:
            case "U":
                y -= 1
            case "D":
                y += 1
            case "R":
                x += 1
            case "L":
                x -= 1
    return infections
    

def solution_b():
    infections = 0
    dir = "U"
    x, y = len(map) // 2, len(map) // 2
    for _ in range(10000000):
        if x not in map:
            map[x] = dict()
        if y not in map[x] or map[x][y] == ".":
            dir = {"U": "L", "L": "D", "D": "R", "R":"U"}[dir]
            map[x][y] = "W"
        elif map[x][y] == "#":
            dir = {"U":"R", "R":"D", "D":"L", "L":"U"}[dir]
            map[x][y] = "F"
        elif map[x][y] == "W":
            map[x][y] = "#"            
            infections += 1
        else:
            dir = {"U":"D", "D":"U", "R":"L", "L":"R"}[dir]
            map[x][y] = "."
        match dir:
            case "U":
                y -= 1
            case "D":
                y += 1
            case "R":
                x += 1
            case "L":
                x -= 1
    return infections

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

