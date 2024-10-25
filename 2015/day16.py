import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

#data = examples[0].input_data
data = input_data

unknown_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

data = data.split("\n")

sues = {int(line.split(" ")[1][:-1]) : {section.split(" ")[-2][:-1] : int(section.split(" ")[-1]) for section in line.split(", ")} for line in data}


def solution_a():
    for sue, household in sues.items():
        possible = True
        for thing, quantity in household.items():
            if unknown_sue[thing] != quantity:
                possible = False
        if possible:
            return sue
                

def solution_b():
    for sue, household in sues.items():
        possible = True
        for thing, quantity in household.items():
            match thing:
                case "cats" | "trees":
                    not_fit = unknown_sue[thing] >= quantity
                case "pomeranians" | "goldfish":
                    not_fit = unknown_sue[thing] <= quantity
                case _:
                    not_fit = unknown_sue[thing] != quantity
            if not_fit:
                possible = False
        if possible:
            return sue

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

