from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=2)
data = puzzle.input_data.split("\n")

pos = [0, 0] # i = 0 is depth, i = 1 is hoz pos
for line in data:
    match line.split(" ")[0]:
        case "forward":
            pos[1] += int(line.split(" ")[1])
        case "up":
            pos[0] -= int(line.split(" ")[1])
        case "down":
            pos[0] += int(line.split(" ")[1])
puzzle.answer_a = pos[0] * pos[1]
print(f"Part 1: {pos[0] * pos[1]}")

pos = [0, 0, 0] # i = 0 is depth, i = 1 is hoz pos, i = 2 is aim
for line in data:
    match line.split(" ")[0]:
        case "forward":
            pos[1] += int(line.split(" ")[1])
            pos[0] += int(line.split(" ")[1]) * pos[2]
        case "up":
            pos[2] -= int(line.split(" ")[1])
        case "down":
            pos[2] += int(line.split(" ")[1])
puzzle.answer_b = pos[0] * pos[1]
print(f"Part 2: {pos[0] * pos[1]}")