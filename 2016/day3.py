import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603"""
data = input_data

data = data.split("\n")
data = [[int(x) for x in line.split()] for line in data]

def solution_a():
    triangles = data
    valid = 0
    for a, b, c in triangles:
        if a + b > c and a + c > b and b + c > a:
            valid += 1
    return valid

def solution_b():
    triangles = []
    for i in range(0, len(data), 3):
        a1, b1, c1 = data[i]
        a2, b2, c2 = data[i + 1]
        a3, b3, c3 = data[i + 2]
        triangles.append([a1, a2, a3])
        triangles.append([b1, b2, b3])
        triangles.append([c1, c2, c3])
    valid = 0
    for a, b, c in triangles:
        if a + b > c and a + c > b and b + c > a:
            valid += 1
    return valid

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

