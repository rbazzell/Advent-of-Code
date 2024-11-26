import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data: str = examples[0].input_data
data: str = input_data

data = data.split("\n")
instructions = []
for line in data:
    reg_m, command, value, iN, reg_c, ineq, target = line.split()
    instructions.append((reg_m, command, int(value), reg_c, ineq, int(target)))

def solution_a():
    registers = dict()
    for m, command, v, c, ineq, t in instructions:
        if not registers.get(m):
            registers[m] = 0
        if not registers.get(c):
            registers[c] = 0
        if command == "dec":
            v = -v
        match ineq:
            case "==":
                if registers[c] == t:
                    registers[m] += v
            case "!=":
                if registers[c] != t:
                    registers[m] += v
            case ">":
                if registers[c] > t:
                    registers[m] += v
            case ">=":
                if registers[c] >= t:
                    registers[m] += v
            case "<":
                if registers[c] < t:
                    registers[m] += v
            case "<=":
                if registers[c] <= t:
                    registers[m] += v
    return max(registers.values())

def solution_b():
    registers = dict()
    max_reg = 0
    for m, command, v, c, ineq, t in instructions:
        if not registers.get(m):
            registers[m] = 0
        if not registers.get(c):
            registers[c] = 0
        if command == "dec":
            v = -v
        match ineq:
            case "==":
                if registers[c] == t:
                    registers[m] += v
            case "!=":
                if registers[c] != t:
                    registers[m] += v
            case ">":
                if registers[c] > t:
                    registers[m] += v
            case ">=":
                if registers[c] >= t:
                    registers[m] += v
            case "<":
                if registers[c] < t:
                    registers[m] += v
            case "<=":
                if registers[c] <= t:
                    registers[m] += v
        max_reg = max(registers[m], max_reg)
    return max_reg

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

