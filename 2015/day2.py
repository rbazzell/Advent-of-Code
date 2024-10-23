import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
gifts = [[int(x) for x in y.split("x")] for y in data]
for gift in gifts:
    gift.sort()

def solution_a():
    paper = 0
    for l, w, h in gifts:
        paper += 2*(l*w + w*h + h*l) + (l*w)
    return paper

def solution_b():
    ribbon = 0
    for l, w, h in gifts:
        ribbon += l*w*h + 2*(l+w)
    return ribbon

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

