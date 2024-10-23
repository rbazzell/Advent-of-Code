import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
import copy

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

data = [[x.split()[0], int(x.split()[1]), 0] for x in data]
# access is data[instruction][0 for opcode, 1 for offset, 2 for # of runs]

def solution_a():
    instructions = copy.deepcopy(data)
    acc = 0
    pc = 0
    instruction = instructions[pc]
    while instruction[2] < 1:
        match instruction[0]:
            case "acc":
                acc += instruction[1]
                pc += 1
            case "jmp":
                pc += instruction[1]
            case "nop":
                pc += 1
        instruction[2] += 1
        instruction = instructions[pc]
    return acc


def solution_b():
    for i in range(len(data)):
        instructions = copy.deepcopy(data)
        match instructions[i][0]:
            case "acc":
                continue
            case "jmp":
                instructions[i][0] = "nop"
            case "nop":
                instructions[i][0] = "jmp"
        acc = 0
        pc = 0
        instruction = instructions[pc]
        while instruction[2] < 1:
            match instruction[0]:
                case "acc":
                    acc += instruction[1]
                    pc += 1
                case "jmp":
                    pc += instruction[1]
                case "nop":
                    pc += 1
            instruction[2] += 1
            if pc == len(instructions):
                return acc
            instruction = instructions[pc]
        
    return None

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

