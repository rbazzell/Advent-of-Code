import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
import re

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
data = input_data

registers, program = data.split("\n\n")
registers = {x.split()[1][0] : int(x.split()[2]) for x in registers.split("\n")}
program = tuple(int(x) for x in program.split()[1].split(","))

def combo(operand: int, registers):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]

def compute(registers, program):
    buffer: list[int] = list()
    pc = 0
    while 0 <= pc < len(program):
        opcode, operand = program[pc:pc+2]
        match opcode:
            case 0: #adv -combo
                operand = combo(operand, registers)
                registers["A"] >>= operand
            case 1: #bxl -literal
                registers["B"] ^= operand
            case 2: #bst -combo
                operand = combo(operand, registers)
                registers["B"] = operand % 8
            case 3: #jnz -literal
                if registers["A"] != 0:
                    pc = operand - 2
            case 4: #bxc -ignored
                registers["B"] ^= registers["C"]
            case 5: #out -combo
                operand = combo(operand, registers)
                buffer.append(operand % 8)
            case 6: #bdv -combo
                operand = combo(operand, registers)
                registers["B"] = registers["A"] >> operand
            case 7: #cdv -combo
                operand = combo(operand, registers)
                registers["C"] = registers["A"] >> operand
        pc += 2
    return buffer

def solution_a():
    buffer = compute(registers.copy(), program)
    return ",".join(str(x) for x in buffer)

def recursive_check(a: int, j: int):
    if j == -1:
        return a
    for i in range(8):
        regs = registers.copy()
        regs["A"] = (a << 3) + i
        buffer = compute(regs, program)
        if buffer[0] == program[j]:
            x = recursive_check((a << 3) + i, j - 1)
            if x:
                return x
    return None

def solution_b():
    return recursive_check(0, len(program) - 1)


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

