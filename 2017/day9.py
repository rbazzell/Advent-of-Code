import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[14].input_data
data = input_data

S = data

def solution_a():
    score = 0
    open_groups = 0
    in_garbage = False
    i = 0
    while i < len(S):
        if not in_garbage:
            match S[i]:
                case "{":
                    open_groups += 1
                case "}":
                    score += open_groups
                    open_groups -= 1
                case "<":
                    in_garbage = True
        else:
            match S[i]:
                case "!":
                    i += 1
                case ">":
                    in_garbage = False
        i += 1
    return score

        

def solution_b():
    garbage_count = 0
    in_garbage = False
    i = 0
    while i < len(S):
        if not in_garbage:
            match S[i]:
                case "<":
                    in_garbage = True
        else:
            match S[i]:
                case "!":
                    i += 1
                case ">":
                    in_garbage = False
                case _:
                    garbage_count += 1
        i += 1
    return garbage_count

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

