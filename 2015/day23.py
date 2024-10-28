import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
instructions = dict()
for i, line in enumerate(data):
    instructions[i] = [int(x) if x[0] in ("+", "-") else x for x in line.replace(",", "").split(" ")]

def compute(a:int, b:int):
    regs = {"a": a, "b": b}
    instruction = instructions[0]
    curr = 0
    while instruction != None:
        command = instruction[0]
        register = None if command == "jmp" else instruction[1]
        offset = instruction[2] if command in ("jie", "jio") else instruction[1] if command == "jmp" else None
        match instruction[0]:
            case "hlf":
                regs[register] //= 2
            case "tpl":
                regs[register] *= 3
            case "inc":
                regs[register] += 1
            case "jmp":
                curr += offset - 1
            case "jie":
                if regs[register] % 2 == 0:
                    curr += offset - 1
            case "jio":
                if regs[register] == 1:
                    curr += offset - 1
        curr += 1
        instruction = instructions.get(curr)
    return regs


def solution_a():
    return compute(0, 0)['b']
    

def solution_b():
    return compute(1, 0)['b']

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

