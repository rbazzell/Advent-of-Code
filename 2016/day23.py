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
    line: list[str] = line.split(" ")
    command = line[0]
    match command:
        case "inc" | "dec":
            arg1 = line[1]
            arg2 = None
        case "tgl":
            if line[1].isdigit() or line[1][1:].isdigit():
                arg1 = int(line[1])
            else:
                arg1 = line[1]
            arg2 = None
        case "cpy":
            if line[1].isdigit() or line[1][1:].isdigit():
                arg1 = int(line[1])
            else:
                arg1 = line[1]
            arg2 = line[2]
        case "jnz":
            if line[1].isdigit() or line[1][1:].isdigit():
                arg1 = int(line[1])
            else:
                arg1 = line[1]
            if line[2].isdigit() or line[2][1:].isdigit():
                arg2 = int(line[2])
            else:
                arg2 = line[2]
    match command:
        case "inc" | "dec" | "tgl" | "jnz":
            if isinstance(arg1, str) and arg1 not in registers.keys():
                registers[arg1] = 0
        case "cpy":
            if isinstance(arg2, str) and arg2 not in registers.keys():
                registers[arg2] = 0
    instruction = (command, arg1, arg2)
    instructions.append(instruction)

def compute(instructions, registers):
    pc = 0
    while pc < len(instructions):
        command, arg1, arg2 = instructions[pc]
        if pc == 10:
            pass

        if pc + 6 < len(instructions)  and [instruction[0] for instruction in instructions[pc:pc+6]] ==  ["cpy", "inc", "dec", "jnz", "dec", "jnz"]:
            arg1 = arg1
            arg2 = instructions[pc+5][1]
            arg3 = instructions[pc+1][1]
            if not isinstance(arg1, int):
                arg1 = registers[arg1]
            if not isinstance(arg2, int):
                arg2 = registers[arg2]
            registers[arg3] = arg1 * arg2
            pc += 6
            continue
        match command:
            case "cpy":
                if isinstance(arg2, str):
                    if not isinstance(arg1, int):
                        arg1 = registers[arg1]
                    registers[arg2] = arg1
            case "inc":
                if isinstance(arg1, str):
                    registers[arg1] += 1
            case "dec":
                if isinstance(arg1, str):
                    registers[arg1] -= 1
            case "jnz":
                if not isinstance(arg1, int):
                    arg1 = registers[arg1]
                if not isinstance(arg2, int):
                    arg2 = registers[arg2]
                if arg1 != 0:
                    pc += arg2
                    continue
            case "tgl":
                if not isinstance(arg1, int):
                    arg1 = registers[arg1]
                if pc + arg1 < len(instructions):
                    instructions[pc + arg1] = toggle_instruction(*instructions[pc + arg1])
        pc += 1
    return registers["a"]

def toggle_instruction(command, offset, register):
    match command:
        case "inc":
            command = "dec"
        case "dec" | "tgl":
            command = "inc"
        case "jnz":
            command = "cpy"
        case "cpy":
            command = "jnz"
    return (command, offset, register)

def solution_a():
    r = registers.copy()
    r['a'] = 7
    return compute(instructions, r)

def solution_b():    
    r = registers.copy()
    r['a'] = 12
    return compute(instructions, r)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

