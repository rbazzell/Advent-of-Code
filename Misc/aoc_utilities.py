from aocd.models import Puzzle
from aocd.examples import Example
import os

def get_puzzle(file:str):
    day = int(file.split("\\")[-1][3:-3])
    year = int(file.split("\\")[-2])
    with open("misc\\session_token.txt") as f:
            os.environ["AOC_SESSION"] = f.read()
    return Puzzle(year=year, day=day)

def check_example(puzzle, i, ans, partb=False):
    if not partb:
        return puzzle.examples[i].answer_a == ans
    else:
        return puzzle.examples[i].answer_b == ans
def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print()

def grid_str(grid):
    s = ""
    for row in grid:
        for col in row:
            s += col
        s += "\n"
    return s

        
