import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[1].input_data
data = input_data

data = data.replace(" bags", "").replace(" bag", "").replace(".","").split("\n")
#data should be a dictionary
#{"red" : [(1, "white"), (2, "yellow")]}

bags = dict()
for line in data:
    inside = list()
    for bag in line.split(" contain ")[1].split(", "):
        if bag[0] != 'n':
            inside.append((int(bag[0]), bag[2:]))
    bags[line.split(" contain ")[0]] = inside

def solution_a():
    golden = bags.copy()
    for key in golden.keys():
        golden[key] = -1 # -1 mean unevaluated, 0 means no golden, 1 means golden
    for bag in bags.keys():
        explore(bags, golden, bag)
    return sum(golden.values())

def explore(bags, golden, key):
    if golden[key] != -1: #This bag has already been evaluated
        return
    golden[key] = 0 #by default, we assume no gold
    for bag in bags[key]:
        if bag[1] == "shiny gold": #This bag directly has a golden
            golden[key] = 1
            return
        if golden[bag[1]] == -1: #checks to see if the interior bags haven't been evaluated
            explore(bags, golden, bag[1])
        golden[key] |= golden[bag[1]] # if there is a gold, it will or with this to set this one as having a gold
    return

def solution_b():
    return search(bags, "shiny gold")

def search(bags, key):
    contains = 0
    for bag in bags[key]:
        contains += bag[0] * search(bags, bag[1]) + bag[0]
    return contains

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

