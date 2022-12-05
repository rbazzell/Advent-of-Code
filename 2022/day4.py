from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=4)
#data = puzzle.example_data
data = puzzle.input_data


def contains(x, y):
    if x[0] <= y[0] and x[-1] >= y[-1]:
        return True
    elif x[0] >= y[0] and x[-1] <= y[-1]:
        return True
    return False

def overlaps(x, y):
    return bool(list(set(x) & set(y)))


data = [line.split(",") for line in data.split("\n")]
for line in data:
    line[0] = range(int(line[0].split("-")[0]), int(line[0].split("-")[-1]) + 1)
    line[1] = range(int(line[1].split("-")[0]), int(line[1].split("-")[-1]) + 1)

contain = 0
overlap = 0
for line in data:
    if overlaps(line[0], line[1]):
        overlap += 1
        if contains(line[0], line[1]):
            contain += 1
    



print(f"a: {contain}")
#puzzle.answer_a = contain

print(f"b: {overlap}")
puzzle.answer_b = overlap