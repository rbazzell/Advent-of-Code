from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=1)
data = [int(x) for x in puzzle.input_data.split("\n")]

increased = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        increased += 1
puzzle.answer_a = increased
print(f"Part 1: {increased}")

increased = 0
for i in range(3, len(data)):
    if data[i] + data[i - 1] + data[i - 2] > data[i - 1] + data[i - 2] + data[i - 3]:
        increased += 1
puzzle.answer_b = increased
print(f"Part 2: {increased}")

