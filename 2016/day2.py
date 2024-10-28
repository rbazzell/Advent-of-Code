import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

keypad = {0:{0:"7",1:"8",2:"9"},
          1:{0:"4",1:"5",2:"6"},
          2:{0:"1",1:"2",2:"3"}}

starpad = {2:                  {0:"1"},
           1:          {-1:"2", 0:"3", 1:"4"},
           0:  {-2:"5", -1:"6", 0:"7", 1:"8", 2:"9"},
           -1:         {-1:"A", 0:"B", 1:"C"},
           -2:                 {0:"D"}}

def solution_a():
    code = ""
    x, y = 1, 1
    for path in data:
        for move in path:
            match move:
                case "U":
                    y = min(2, y + 1)
                case "R":
                    x = min(2, x + 1)
                case "D":
                    y = max(0, y - 1)
                case "L":
                    x = max(0, x - 1)
        code += keypad[y][x]
    return code

def solution_b():
    code = ""
    x, y = -2, 0
    for path in data:
        for move in path:
            match move:
                case "U":
                    if sum((abs(x), abs(y + 1))) <= 2:
                        y = min(2, y + 1)
                case "R":
                    if sum((abs(x + 1), abs(y))) <= 2:
                        x = min(2, x + 1)
                case "D":
                    if sum((abs(x), abs(y - 1))) <= 2:
                        y = max(-2, y - 1)
                case "L":
                    if sum((abs(x - 1), abs(y))) <= 2:
                        x = max(-2, x - 1)
        code += starpad[y][x]
    return code


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

