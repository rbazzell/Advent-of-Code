import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

xmas = [int(x) for x in data]




def solution_a():
    pal = 25
    for i in range(pal, len(xmas)):
        found = False
        for j in range(i - pal, i):
            num = xmas[i] - xmas[j]
            if num in xmas[i-pal:i] and xmas[i-pal:i].index(num) != j:
                found = True
                break
        if not found:
            return xmas[i]


def solution_b():
    target = solution_a()
    for i in range(len(xmas)):
        sum = xmas[i]
        j = i + 1
        while sum < target:
            sum += xmas[j]
            j += 1
            if sum == target:
                return min(xmas[i:j]) + max(xmas[i:j])

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

