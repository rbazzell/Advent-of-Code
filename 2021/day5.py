from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=5)
data = puzzle.input_data


def hoz_line(grid, x1, x2, y):
    for i in range(min(x1, x2), max(x1, x2) + 1):
        grid[y][i] += 1


def vert_line(grid, y1, y2, x):
    for i in range(min(y1, y2), max(y1, y2) + 1):
        grid[i][x] += 1


def diag_line(grid, x1, x2, y1, y2):
    for i in range(max(x1, x2) - min(x1, x2) + 1):
        if y1 < y2 and x1 < x2:
            grid[y1 + i][x1 + i] += 1
        elif y2 < y1 and x2 < x1: # no need to check == b/c it would be caught by hoz
            grid[y2 + i][x2 + i] += 1
        elif y1 < y2 and x2 < x1:
            grid[y1 + i][x1 - i] += 1
        else:
            grid[y2 + i][x2 - i] += 1

def print_grid(grid):
    for row in grid:
        for num in row:
            if num == 0:
                print(".", end="")
            else:
                print(num, end="")
        print()


x1 = [int(line.split(" -> ")[0].split(",")[0]) for line in data.split("\n")]
y1 = [int(line.split(" -> ")[0].split(",")[1]) for line in data.split("\n")]
x2 = [int(line.split(" -> ")[1].split(",")[0]) for line in data.split("\n")]
y2 = [int(line.split(" -> ")[1].split(",")[1]) for line in data.split("\n")]

grid_size_y = max(x1 + x2)
grid_size_x = max(y1 + y2)

grid_a = [[0 for i in range(grid_size_x + 1)] for j in range(grid_size_y + 1)]
grid_b = [[0 for i in range(grid_size_x + 1)] for j in range(grid_size_y + 1)]

for i in range(len(x1)):
    if x1[i] == x2[i]:
        vert_line(grid_a, y1[i], y2[i], x1[i])
        vert_line(grid_b, y1[i], y2[i], x1[i])
    elif y1[i] == y2[i]:
        hoz_line(grid_a, x1[i], x2[i], y1[i])
        hoz_line(grid_b, x1[i], x2[i], y1[i])
    else:
        diag_line(grid_b, x1[i], x2[i], y1[i], y2[i])

count_a = 0
for row in grid_a:
    for num in row:
        if num > 1:
            count_a += 1

puzzle.answer_a = count_a
print(f"Part 1: {count_a}")
count_b = 0
for row in grid_b:
    for num in row:
        if num > 1:
            count_b += 1
puzzle.answer_b = count_b
print(f"Part 2: {count_b}")