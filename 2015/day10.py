import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[1].input_data
data = input_data

def look_and_say(n:str):
    result = ""
    curr = n[0]
    count = 1
    for i in range(1, len(n)):
        if n[i] != curr:
            result += f"{count}{curr}"
            count = 1
            curr = n[i]
        else:
            count += 1
    result += f"{count}{curr}"
    return result

def solution_a():
    input = data
    for i in range(40):
        input = look_and_say(input)
    return len(input)

def solution_b():
    input = data
    for i in range(50):
        input = look_and_say(input)
    return len(input)

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

