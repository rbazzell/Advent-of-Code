from aocd.models import Puzzle
import os, re
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

def slow_part_b(): #my design, wayyyy too slow
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
    return ans_b


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

def calc_y_intercept(slope: int, x1: int, y1: int):
    return y1 - slope * x1

def find_intersection(line1: tuple[int, int], line2: tuple[int, int]):
    if line1 == line2:
        raise Exception("line1 and line2 are the same")
    x = (line1[1] - line2[1]) // (line2[0] - line1[0])
    y = line1[0] * x + line1[1]
    return (x, y)

def add_to_lines(lines: list, count: list[int], slope: int, b: int):
    line = (slope, b)
    if line in lines:
        count[lines.index(line)] += 1
    else:
        lines.append(line)
        count.append(1)
    return lines, count

def check_excluded(point: tuple[int, int]):
    for set in data:
        signal_range = manhat(set['S'], set['B'])
        point_range = manhat(set['S'], point)
        if signal_range >= point_range:
            return False
    return True

def part_a():
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
    return target_row.count("#")



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


#ans_b = slow_part_b()


# the math for this part b solution comes from BuonHobo on Github: https://github.com/BuonHobo/advent-of-code/blob/master/2022/15/Alex/second.py
# however, all the code here is my own, I did not use his code, just his math
lines: list[tuple[int, int]] = [] # fthe first int is slope (-1 or 1), the second int is the y intercept
count: list[int] = []

for set in data:
    manhattan = manhat(set['S'], set['B'])
    lines, count = add_to_lines(lines, count, 1, calc_y_intercept(1, set['S'][0] + manhattan + 1, set['S'][1]))
    lines, count = add_to_lines(lines, count, 1, calc_y_intercept(1, set['S'][0] - manhattan - 1, set['S'][1]))
    lines, count = add_to_lines(lines, count, -1, calc_y_intercept(-1, set['S'][0] + manhattan + 1, set['S'][1]))
    lines, count = add_to_lines(lines, count, -1, calc_y_intercept(-1, set['S'][0] - manhattan - 1, set['S'][1]))

pointer = 0
while 1 in count:
    if count[pointer] == 1:
        count.pop(pointer)
        lines.pop(pointer)
    else:
        pointer += 1

points: list[tuple[int, int]] = []
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if lines[i][0] != lines[j][0]:
            point = find_intersection(lines[i], lines[j])
            if point not in points:
                points.append(point)
ans_b = -1
for point in points:
    if 0 <= point[0] <= target[1] and 0 <= point[1] <= target[1] and check_excluded(point):
        ans_b = 4000000 * point[0] + point[1]
        break
    


ans_a = "Not now"
#ans_a = part_a()
print(f"a: {ans_a}")
#puzzle.answer_a = ans_a

print(f"b: {ans_b}")
puzzle.answer_b = ans_b