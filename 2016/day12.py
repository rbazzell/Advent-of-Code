import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

registers = dict()
instructions: list[tuple] = []
for line in data:
    line = line.split(" ")
    command = line[0]
    match command:
        case "cpy":
            register = line[2]
            if line[1].isdigit():
                offset = int(line[1])
            else:
                offset = line[1]
        case "inc" | "dec":
            register = line[1]
            offset = 0
        case "jnz":
            if line[1].isdigit():
                register = int(line[1])
            else:
                register = line[1]
            offset = int(line[2])
    if register not in registers.keys():
        registers[register] = 0
    instruction = (command, offset, register)
    instructions.append(instruction)

def compute(instructions, registers):
    pc = 0
    while pc < len(instructions):
        command, offset, register = instructions[pc]
        match command:
            case "cpy":
                if not isinstance(offset, int):
                    offset = registers[offset]
                registers[register] = offset
            case "inc":
                registers[register] += 1
            case "dec":
                registers[register] -= 1
            case "jnz":
                if not isinstance(register, int):
                    register = registers[register]
                if register != 0:
                    pc += offset - 1
        pc += 1
    return registers["a"]


def solution_a():
    return compute(instructions, registers.copy())
                

def solution_b():
    regs = registers.copy()
    regs["c"] = 1
    return compute(instructions, regs)


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

