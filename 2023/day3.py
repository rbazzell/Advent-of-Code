from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f8bff693a28ddc555a8233386bd6b1ad7e554d5c83830f2ea1712910385002a2567dd54ec3ae2321a7cb563c5dda138661eb4b1697bc4f472" # handout: exclude


def parse_input(data):
    return data.split(), [[False for x in line] for line in data.split()], [[False for x in line] for line in data.split()]


def mult_nums(nums):
    if len(nums) != 2:
        return 0
    return nums[0] * nums[1]

def check_symbol(grid, check, r, c, symbol=""):
    if symbol and grid[r][c] != symbol:
        return 0
    rl = len(grid)
    cl = len(grid[0])
    total = 0
    if (is_valid_position(r-1, c-1, rl, cl) and grid[r-1][c-1].isdigit()):
        total += check_off(grid, check, r-1, c-1)
    if (is_valid_position(r-1, c, rl, cl) and grid[r-1][c].isdigit()):
        total += check_off(grid, check, r-1, c)
    if (is_valid_position(r-1, c+1, rl, cl) and grid[r-1][c+1].isdigit()):
        total += check_off(grid, check, r-1, c+1)
    if (is_valid_position(r, c+1, rl, cl) and grid[r][c+1].isdigit()):
        total += check_off(grid, check, r, c+1)
    if (is_valid_position(r+1, c+1, rl, cl) and grid[r+1][c+1].isdigit()):
        total += check_off(grid, check, r+1, c+1)
    if (is_valid_position(r+1, c, rl, cl) and grid[r+1][c].isdigit()):
        total += check_off(grid, check, r+1, c)
    if (is_valid_position(r+1, c-1, rl, cl) and grid[r+1][c-1].isdigit()):
        total += check_off(grid, check, r+1, c-1)
    if (is_valid_position(r, c-1, rl, cl) and grid[r][c-1].isdigit()):
        total += check_off(grid, check, r, c-1)
    return total


def check_asterick(grid, check, r, c):
    if grid[r][c] != '*':
        return 0
    rl = len(grid)
    cl = len(grid[0])
    nums = []
    if (is_valid_position(r-1, c-1, rl, cl) and grid[r-1][c-1].isdigit()):
        nums.append(check_off(grid, check, r-1, c-1, -1))
    if (is_valid_position(r-1, c, rl, cl) and grid[r-1][c].isdigit()):
        nums.append(check_off(grid, check, r-1, c, -1))
    if (is_valid_position(r-1, c+1, rl, cl) and grid[r-1][c+1].isdigit()):
        nums.append(check_off(grid, check, r-1, c+1, -1))
    if (is_valid_position(r, c+1, rl, cl) and grid[r][c+1].isdigit()):
        nums.append(check_off(grid, check, r, c+1, -1))
    if (is_valid_position(r+1, c+1, rl, cl) and grid[r+1][c+1].isdigit()):
        nums.append(check_off(grid, check, r+1, c+1, -1))
    if (is_valid_position(r+1, c, rl, cl) and grid[r+1][c].isdigit()):
        nums.append(check_off(grid, check, r+1, c, -1))
    if (is_valid_position(r+1, c-1, rl, cl) and grid[r+1][c-1].isdigit()):
        nums.append(check_off(grid, check, r+1, c-1, -1))
    if (is_valid_position(r, c-1, rl, cl) and grid[r][c-1].isdigit()):
        nums.append(check_off(grid, check, r, c-1, -1))
    return mult_nums([n for n in nums if n != -1])  


def is_valid_position(r, c, rl, cl):
    return not (r < 0 or r > rl - 1 or c < 0 or c > cl - 1)


def check_off(grid, check, r, c, mul_nadd=0):
    if check[r][c]:
        return mul_nadd
    else:
        i, j = check_num(grid[r], c)
        for k in range(i, j):
            check[r][k] = True
        return int(grid[r][i:j])
    

def check_num(row, c):
    for i in range(c, -1, -1):
        if not row[i].isdigit():
            i += 1
            break
    for j in range(c, len(row)):
        if not row[j].isdigit():
            j -= 1
            break
    return i, j + 1

puzzle = Puzzle(year=2023, day=3)
#data = puzzle.example_data
data = puzzle.input_data
print(data)
data, check_a, check_b = parse_input(data)



sum_a = 0
sum_b = 0
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c != '.' and not c.isalnum():
            sum_a += check_symbol(data, check_a, i, j)
            sum_b += check_asterick(data, check_b, i, j)

print(f"Answer 1: {sum_a}")
print(f"Answer 2: {sum_b}")


#puzzle.answer_a = sum_a
puzzle.answer_b = sum_b