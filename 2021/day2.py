import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

commands = tuple((line.split()[0], int(line.split()[1])) for line in data.split("\n"))

def solution_a():
    hoz, depth = 0, 0
    for command, x in commands:
        match command:
            case "forward":
                hoz += x
            case "down":
                depth += x
            case "up":
                depth -= x
    return hoz * depth
            

def solution_b():
    hoz, depth = 0, 0
    aim = 0
    for command, x in commands:
        match command:
            case "forward":
                hoz += x
                depth += aim * x
            case "down":
                aim += x
            case "up":
                aim -= x
    return hoz * depth

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

