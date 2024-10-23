import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

instructions = []
for line in data:
    instruction = []

    split = line.find(" ")
    if split < 6:
        line = line[split+1:]
        split = line.find(" ")
    instruction.append(line[:split])
    line = line[split+1:]

    line = line.split(" through ")
    instruction.append(tuple(int(x) for x in line[0].split(',')))
    instruction.append(tuple(int(x) for x in line[1].split(',')))
    instructions.append(tuple(instruction))


def solution_a():
    lights = [[0 for i in range(1000)] for j in range(1000)]
    for instruction, start, end in instructions:
        match instruction:
            case "on":
                for i in range(start[0], end[0]+1):
                    for j in range(start[1], end[1]+1):
                        lights[j][i] = 1
            case "off":
                for i in range(start[0], end[0]+1):
                    for j in range(start[1], end[1]+1):
                        lights[j][i] = 0
            case "toggle":
                for i in range(start[0], end[0]+1):
                    for j in range(start[1], end[1]+1):
                        lights[j][i] = not lights[j][i]
    return sum([sum(row) for row in lights])
    

def solution_b():
    lights = [[0 for i in range(1000)] for j in range(1000)]
    for instruction, start, end in instructions:
        match instruction:
            case "on":
                for i in range(start[0], end[0]+1):
                    for j in range(start[1], end[1]+1):
                        lights[j][i] += 1
            case "off":
                for i in range(start[0], end[0]+1):
                    for j in range(start[1], end[1]+1):
                        lights[j][i] -= 1 if lights[j][i] else 0
            case "toggle":
                for i in range(start[0], end[0]+1):
                    for j in range(start[1], end[1]+1):
                        lights[j][i] += 2
    return sum([sum(row) for row in lights])

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

