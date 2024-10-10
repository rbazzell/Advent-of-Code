from aocd.models import Puzzle
from aocd.examples import Example
import os


def get_puzzle(day, year):
    with open("misc\\session_token.txt") as f:
            os.environ["AOC_SESSION"] =  f.read()
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

        
