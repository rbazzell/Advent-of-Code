from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=7)
data = puzzle.input_data
data = [int(x) for x in data.split(",")]

positions = [0 for i in range(max(data) + 1)]
for pos in data:
    positions[pos] += 1

min_fuel = 0xFFFFFFF
for i in range(len(positions)):
    fuel = 0
    for j in range(len(positions)):
        fuel += abs(j - i) * positions[j]
    if min_fuel > fuel:
        min_fuel = fuel

puzzle.answer_a = min_fuel
print(f"Part 1: {min_fuel}")

min_fuel = 0xFFFFFFF
for i in range(len(positions)):
    fuel = 0
    for j in range(len(positions)):
        fuel += abs(j - i) * (abs(j - i) + 1) // 2 * positions[j]
    if min_fuel > fuel:
        min_fuel = fuel
puzzle.answer_b = min_fuel
print(f"Part 2: {min_fuel}")

