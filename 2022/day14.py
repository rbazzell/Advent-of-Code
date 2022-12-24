from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

def print_walls(walls):
    for row in walls:
        for point in row:
            print(point, end="")
        print()  

def can_move(curr: tuple, walls: list, offset: int):
    if walls[curr[1] + 1][curr[0] - offset] == ".":
        return 1
    elif walls[curr[1] + 1][curr[0] - 1 - offset] == ".":
        return 2
    elif walls[curr[1] + 1][curr[0] + 1 - offset] == ".":
        return 3
    return 0

puzzle = Puzzle(year=2022, day=14)
data = puzzle.example_data
data = puzzle.input_data
data = [[(int(point.split(",")[0]), int(point.split(",")[1])) for point in line.split(" -> ")] for line in data.split("\n")]
max_y = 0
for line in data:
    for coord in line:
        if coord[1] > max_y:
            max_y = coord[1]
#walls[y][x]
offset = 500 - max_y - 2
walls = [["." for j in range(offset, 500 + max_y + 3)] for i in range(max_y + 4)]
walls[0][500 - offset] = "+"
for line in data:
    for i in range(len(line) - 1):
        if line[i][0] == line[i + 1][0] and line[i][1] < line[i + 1][1]:
            for j in range(line[i][1], line[i + 1][1] + 1):
                walls[j][line[i][0] - offset] = "#"
        elif line[i][0] == line[i + 1][0] and line[i][1] > line[i + 1][1]:
            for j in range(line[i][1], line[i + 1][1] - 1, -1):
                walls[j][line[i][0] - offset] = "#"
        elif line[i][1] == line[i + 1][1] and line[i][0] < line[i + 1][0]:
            for j in range(line[i][0], line[i + 1][0] + 1):
                walls[line[i][1]][j - offset] = "#"
        else:
            for j in range(line[i][0], line[i + 1][0] - 1, -1):
                walls[line[i][1]][j - offset] = "#"

ans_a = 0
while True:
    #print_walls(walls)
    curr = (500, 0)
    while can_move(curr, walls, offset):
        match can_move(curr, walls, offset):
            case 1:
                curr = (curr[0], curr[1] + 1)
            case 2:
                curr = (curr[0] - 1, curr[1] + 1)
            case 3:
                curr = (curr[0] + 1, curr[1] + 1)
        if curr[1] >= max_y:
            break
    else:
        walls[curr[1]][curr[0] - offset] = "O"
        ans_a += 1
        continue
    break

for i in range(len(walls)):
    for j in range(len(walls[i])):
        if i == max_y + 2:
            walls[i][j] = "#"
        elif walls[i][j] == "O":
            walls[i][j] = "."
ans_b = 0
while curr != (500, 0):
    curr = (500, 0)
    while can_move(curr, walls, offset):
        match can_move(curr, walls, offset):
            case 1:
                curr = (curr[0], curr[1] + 1)
            case 2:
                curr = (curr[0] - 1, curr[1] + 1)
            case 3:
                curr = (curr[0] + 1, curr[1] + 1)
    walls[curr[1]][curr[0] - offset] = "O"
    ans_b += 1

print(f"a: {ans_a}")
puzzle.answer_a = ans_a

print(f"b: {ans_b}")
puzzle.answer_b = ans_b
