import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[2].input_data
data = input_data

data = [(x[0], int(x[1:])) for x in data.split(", ")]



def solution_a():
    x, y = 0, 0
    facing = 0 #0 is north
    for turn, walk in data:
        if turn == "R":
            facing += 1
        else:
            facing -= 1
        facing %= 4

        match facing:
            case 0:
                y += walk
            case 1:
                x += walk
            case 2:
                y -= walk
            case 3:
                x -= walk
    return abs(x) + abs(y)

def solution_b():
    x, y = 0, 0
    facing = 0 #0 is north
    previous = [(x, y)]
    for turn, walk in data:
        if turn == "R":
            facing += 1
        else:
            facing -= 1
        facing %= 4
        for step in range(walk):
            match facing:
                case 0:
                    y += 1
                case 1:
                    x += 1
                case 2:
                    y -= 1
                case 3:
                    x -= 1
            if (x, y) in previous:
                return abs(x) + abs(y)
            else:
                previous.append((x, y))
    return -1
    

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

