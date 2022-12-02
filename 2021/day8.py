from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=8)
data = puzzle.input_data

output = [[x for x in line.split(" | ")[1].split()] for line in data.split("\n")]

count = 0
for line in output:
    for code in line:
        if len(code) == 2 or len(code) == 3 or len(code) == 4 or len(code) == 7:
            count += 1

puzzle.answer_a = count
print(f"Part 1: {count}")