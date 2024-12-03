import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
data = input_data

memory: str = data

def solution_a():
    total = 0
    i = 0
    while i < len(memory):
        if memory[i:i+4] == "mul(":
            i += 4
            c = memory.find(")", i)
            if c <= i + 8:
                segment = memory[i:c].split(",")
                if len(segment) == 2 and segment[0].isdigit() and segment[1].isdigit():
                    total += int(segment[0]) * int(segment[1])
                i = c
        i += 1
    return total


def solution_b():
    enabled = True
    total = 0
    i = 0
    while i < len(memory):
        if enabled and memory[i:i+4] == "mul(":
            i += 4
            c = memory.find(")", i)
            if c <= i + 8:
                segment = memory[i:c].split(",")
                if len(segment) == 2 and segment[0].isdigit() and segment[1].isdigit():
                    total += int(segment[0]) * int(segment[1])
                i = c
        elif memory[i:i+4] == "do()":
            enabled = True
            i += 3
        elif memory[i:i+7] == "don't()":
            enabled = False
            i += 6
        i += 1
    return total


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

