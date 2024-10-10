import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(1, 2020)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
data = [int(x) for x in data]

def solution_a(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == 2020:
                ans = data[i] * data[j]
                return ans

def solution_b(data):
    for i in range(len(data) - 2):
        for j in range(i + 1, len(data) - 1):
            for k in range(j + 1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    ans = data[i] * data[j] * data[k]
                    return ans


print(solution_b(data))
#puzzle.answer_a = solution_a(data)
puzzle.answer_b = solution_b(data)

