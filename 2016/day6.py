import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
position = ["" for i in range(len(data[0]))]
for i in range(len(data[0])):
    for j in range(len(data)):
        position[i] += data[j][i]

def solution_a():
    output = ""
    for column in position:
        output += max(column, key=column.count)
    return output

def solution_b():
    output = ""
    for column in position:
        output += min(column, key=column.count)
    return output

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

