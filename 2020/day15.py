import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(15, 2020)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = [int(x) for x in data.split(",")]


def solution_a():
    history = dict()
    prev = 0
    curr = data[-1]
    for i in range(len(data) - 1):
        history[data[i]] = i
        #print(f"Turn {i + 1} : {data[i]}")
    for i in range(len(data) - 1, 2020):
        prev = curr
        #print(f"Turn {i + 1} : {curr}")
        if curr in history.keys():
            curr = i - history[curr]
        else:
            curr = 0
        history[prev] = i
    return prev

def solution_b():
    history = dict()
    prev = 0
    curr = data[-1]
    for i in range(len(data) - 1):
        history[data[i]] = i
    for i in range(len(data) - 1, 30000000):
        prev = curr
        if curr in history.keys():
            curr = i - history[curr]
        else:
            curr = 0
        history[prev] = i
    return prev

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

