import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data, width, height = examples[0].input_data, 11, 7
data, width, height = input_data, 101, 103

robots = []
for line in data.split("\n"):
    ps, vs = line.split(" ")
    px, py = int(ps.split(",")[0][2:]), int(ps.split(",")[1])
    vx, vy = int(vs.split(",")[0][2:]), int(vs.split(",")[1])
    robots.append((px, py, vx, vy))

def solution_a():
    time = 100
    quadrants = {1:0, 2:0, 3:0, 4:0}
    for px, py, vx, vy in robots:
        x = (px + vx * time) % width
        y = (py + vy * time) % height
        if x < width // 2 and y < height // 2:
            quadrants[1] += 1
        elif x > width // 2 and y < height // 2:
            quadrants[2] += 1
        elif x < width // 2 and y > height // 2:
            quadrants[3] += 1
        elif x > width // 2 and y > height // 2:
            quadrants[4] += 1
    return quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4]

def solution_b():
    buffer = ""
    for time in range(10000):
        buffer += f"t={time}\n"
        grid = [["." for _ in range(width)] for _ in range(height)]
        for px, py, vx, vy in robots:
            x = (px + vx * time) % width
            y = (py + vy * time) % height
            grid[y][x] = "#"
        buffer += aocu.grid_str(grid)
    with open("C:\\Users\\rybaz\\My Drive\\Personal Projects\\advent_of_code\\2024\\day14.txt", "w") as f:
        f.write(buffer)
    return "Done"

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

