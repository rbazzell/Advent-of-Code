import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[2].input_data
data = input_data

directions: list[str] = data.split(",")

def solution_a():
    q = r = 0
    for d in directions:
        match d:
            case "n":
                r -= 1
            case "s":
                r += 1
            case "ne":
                q += 1
                r -= 1
            case "sw":
                q -= 1
                r += 1
            case "nw":
                q -= 1
            case "se":
                q += 1
    return (abs(q) + abs(q + r) + abs(r)) // 2



def solution_b():
    max_distance = 0
    q = r = 0
    for d in directions:
        match d:
            case "n":
                r -= 1
            case "s":
                r += 1
            case "ne":
                q += 1
                r -= 1
            case "sw":
                q -= 1
                r += 1
            case "nw":
                q -= 1
            case "se":
                q += 1
        max_distance = max(max_distance, (abs(q) + abs(q + r) + abs(r)) // 2)
    return max_distance


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

