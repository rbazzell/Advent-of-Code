import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
strings = data.copy()

def solution_a():
    difference = 0
    for line in data:
        literals = len(line)
        line = line[1:-1]
        i = 0
        memory = 0
        while i < len(line):
            memory += 1
            if line[i] == "\\":
                if line[i+1] == "\\" or line[i+1] =="\"":
                    i += 2
                else:
                    i += 4
            else:
                i += 1
        difference += literals - memory
    return difference


def solution_b():
    difference = 0
    for line in data:
        literals = len(line)
        encoded = 2
        for i in range (len(line)):
            encoded += 1
            if line[i] == "\\" or line[i] == "\"":
                encoded += 1
        difference += encoded - literals
    return difference

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

