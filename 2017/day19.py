import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

path: list[list[str]] = [list(line) for line in data.split("\n")]


def solution_a():
    r, c = 0, path[0].index("|")
    dir = "D"
    letters = ""
    while 0 <= r < len(path) and 0 <= c < len(path[r]) and path[r][c] != " ":
        if path[r][c].isalpha():
            letters += path[r][c]
        elif path[r][c] == "+":
            match dir:
                case "D" | "U":
                    if 0 < c - 1 and path[r][c - 1] != " ":
                        dir = "L"
                    else:
                        dir = "R"
                case "L" | "R":
                    if 0 < r - 1 and path[r - 1][c] != " ":
                        dir = "U"
                    else:
                        dir = "D"
        match dir:
            case "D":
                r += 1
            case "U":
                r -= 1
            case "L":
                c -= 1
            case "R":
                c += 1
    return letters

def solution_b():
    r, c = 0, path[0].index("|")
    dir = "D"
    steps = 0
    while 0 <= r < len(path) and 0 <= c < len(path[r]) and path[r][c] != " ":
        steps += 1
        if path[r][c] == "+":
            match dir:
                case "D" | "U":
                    if 0 < c - 1 and path[r][c - 1] != " ":
                        dir = "L"
                    else:
                        dir = "R"
                case "L" | "R":
                    if 0 < r - 1 and path[r - 1][c] != " ":
                        dir = "U"
                    else:
                        dir = "D"
        match dir:
            case "D":
                r += 1
            case "U":
                r -= 1
            case "L":
                c -= 1
            case "R":
                c += 1
    return steps

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

