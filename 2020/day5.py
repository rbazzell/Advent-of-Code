import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(5, 2020)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

rows = [int(''.join(['1' if y == 'B' else '0' for y in x[:7]]), 2) for x in data]
cols = [int(''.join(['1' if y == 'R' else '0' for y in x[-3:]]), 2) for x in data]
seat_ids = [int(''.join('1' if y == 'B' or y == 'R' else '0' for y in x), 2) for x in data]

def solution_a():
    return max(seat_ids)

def solution_b():
    seat_ids.sort()
    for i in range(1, len(seat_ids)):
        if seat_ids[i] - 1 != seat_ids[i - 1]:
            return seat_ids[i] - 1
    return -1

print(solution_b())
puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

