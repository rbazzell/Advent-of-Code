import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data, rows = examples[1].input_data, 10
data, rows = input_data, 40

def solution_a():
    safe = data.count(".")
    row = data
    for iterations in range(1, rows):
        new_row = str()
        for i in range(len(row)):
            left = row[i - 1] if i > 0 else "."
            center = row[i]
            right = row[i + 1] if i < len(row) - 1 else "."
            if left + center + right in ("^^.", ".^^", "^..", "..^"):
                new_row += "^"
            else:
                new_row += "."
        row = new_row
        safe += row.count(".")
    return safe


def solution_b():
    rows = 400000
    safe = data.count(".")
    row = data
    for iterations in range(1, rows):
        new_row = str()
        for i in range(len(row)):
            left = row[i - 1] if i > 0 else "."
            center = row[i]
            right = row[i + 1] if i < len(row) - 1 else "."
            if left + center + right in ("^^.", ".^^", "^..", "..^"):
                new_row += "^"
            else:
                new_row += "."
        row = new_row
        safe += row.count(".")
    return safe

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

