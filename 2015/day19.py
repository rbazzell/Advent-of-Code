import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO"""
data = input_data


data = data.split("\n\n")

replacements = dict()
replacers = dict()
for line in data[0].split("\n"):
    line = line.split(" => ")
    input = line[0]
    output = line[1]
    if replacements.get(input) == None:
        replacements[input] = []
    replacements[input].append(output)
    replacers[output] = input

medicine = data[1]

def solution_a():
    distinct_molecules = set()
    for atom, transform in replacements.items():
        for i in range(0, len(medicine) - len(atom) + 1):
            if medicine[i:i+len(atom)] == atom:
                possibilities = [medicine[0:i] + t + medicine[i+len(atom):] for t in transform]
                distinct_molecules.update(possibilities)
    return len(distinct_molecules)


def solution_b():
    #start with molecule, get a reverse reference replacements dictionary and go backwards until e
    curr = medicine
    step = 0
    while curr != "e":
        step += 1
        for i in range(len(curr) - 1, -1, -1):
            active = True
            for atom, transform in replacers.items():
                if transform == 'e' and curr != atom or i+len(atom) > len(curr):
                    continue
                if curr[i:i+len(atom)] == atom:
                    curr = curr[0:i] + transform + curr[i+len(atom):]
                    active = False
                    break
            if not active:
                break
    return step

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

