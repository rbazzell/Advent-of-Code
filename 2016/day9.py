import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[5].input_data
#data = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
data = input_data

def calc_size(file: str):
    i = 0
    size = 0
    while i < len(file):
        if file[i] == "(":
            rule = ""
            i += 1
            while file[i] != ")":
                rule += file[i]
                i += 1
            i += 1
            rule = rule.split("x")
            length = int(rule[0])
            repeats = int(rule[1])

            #need check for sub rule here 
            size += repeats * calc_size(file[i:i+length])
            i += length
        else:
            size += 1
            i += 1
    return size





def solution_a():
    file = data
    size = 0
    i = 0
    while i < len(file):
        if file[i] == "(":
            rule = ""
            i += 1
            while file[i] != ")":
                rule += file[i]
                i += 1
            i += 1
            rule = rule.split("x")
            length = int(rule[0])
            repeats = int(rule[1])

            size += length * repeats
            i += length
        else:
            size += 1
            i += 1
    return size

def solution_b():
    file = data
    return calc_size(file)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

