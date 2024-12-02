import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data =[[int(x) for x in line.split(" ")] for line in data.split("\n")]



def solution_a():
    safes = 0
    for line in data:
        if safe(line):
            safes += 1
    return safes

def safe(line: list[str]) -> bool:
    inc = line[1] - line[0] > 0
    for i in range(len(line) - 1):
        x, y = line[i], line[i+1]
        if not (1 <= abs(y - x) <= 3 and inc == (y - x > 0)):
            return False
    return True
                 
def solution_b():
    safes = 0
    for line in data:
        if safe(line):
            safes += 1
        else:
            for i in range(len(line)):
                new_line = line[:i] + line[i+1:]
                if safe(new_line):
                    safes += 1
                    break
    return safes
    

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

