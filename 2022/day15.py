from aocd.models import Puzzle
import os, re
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

def spacify(string: str, spaces: int):
    return string + " " * (spaces - len(string))

def print_row(row: list, offset: int):
    print(" " * abs(offset), end="")
    for x in range(0, len(row) + offset, 5):
        print(spacify(f"{x}", 5), end="")
    print()
    for x in row:
        print(x, end="")
    print()

def make_target_row(minimum: int, maximum: int):
    return ["." for i in range(minimum, maximum)]

def manhat(signal: tuple, beacon: tuple):
    return abs(signal[0] - beacon[0]) + abs(signal[1] - beacon[1])

def difference(a: int, b: int):
    return abs(a - b)

def add_range_to_row(range: range, row: list, offset: int):
    for i in range:
        if 0 <= i - offset < len(row) and row[i - offset] == ".":
            row[i - offset] = "#"



puzzle = Puzzle(year=2022, day=15)
data = puzzle.example_data
data = puzzle.input_data
target = (10, 20)
target = (2000000, 4000000)
data = [re.findall(r'-?\d+\.?\d*', line) for line in data.split("\n")] #0 is sensor x, 1 is sensor y, 
data = [{"S": (int(line[0]), int(line[1])), "B": (int(line[2]), int(line[3]))} for line in data]
x_max = 0
x_min = 9999999999
max_manhat = 0
for set in data:
    if manhat(set['S'], set['B']) > max_manhat:
        max_manhat = manhat(set['S'], set['B'])
    if set['S'][0] > x_max:
        x_max = set['S'][0]
    if set['S'][0] < x_min:
        x_min = set['S'][0]
    if set['B'][0] > x_max:
        x_max = set['B'][0]
    if set['B'][0] < x_min:
        x_min = set['B'][0]

x_offset = x_min - max_manhat
target_row = make_target_row(x_min - max_manhat, x_max + max_manhat + 1)
for set in data:
    if set['S'][1] == target[0]:
        target_row[set['S'][0] - x_offset] = "S"
    if set['B'][1] == target[0]:
        target_row[set['B'][0] - x_offset] = "B"
    manhattan = manhat(set['S'], set['B'])
    diff = difference(manhattan, difference(set['S'][1], target[0]))
    if set['S'][1] - manhattan <= target[0] <= manhattan + set['S'][1]:
        add_range_to_row(range(set['S'][0] - diff, set['S'][0] + diff + 1), target_row, x_offset)

ans_a = target_row.count("#")
ans_b = -1
for i in range(target[1] + 1): # will take over a month to calculate, need a better solution. Come back later after figuring out some math
    target_row = make_target_row(0, target[1] + 1)
    for set in data:
        if set['S'][1] == i and 0 <= set['S'][0] <= target[1]:
            target_row[set['S'][0]] = "S"
        if set['B'][1] == i and 0 <= set['B'][0] <= target[1]:
            target_row[set['B'][0]] = "B"
        manhattan = manhat(set['S'], set['B'])
        diff = difference(manhattan, difference(set['S'][1], i))
        if set['S'][1] - manhattan <= i <= manhattan + set['S'][1]:
            add_range_to_row(range(set['S'][0] - diff, set['S'][0] + diff + 1), target_row, 0)
    if target_row.count("."):
        ans_b = target_row.index(".") * 4000000 + i
        break


print(f"a: {ans_a}")
#puzzle.answer_a = ans_a

print(f"b: {ans_b}")
puzzle.answer_b = ans_b