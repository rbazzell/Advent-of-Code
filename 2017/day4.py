import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[4].input_data
data = input_data

data = data.split("\n")
passphrases = [line.split() for line in data]

def solution_a():
    valid = 0
    for passphrase in passphrases:
        if len(set(passphrase)) == len(passphrase):
            valid += 1
    return valid

def solution_b():
    valid = 0
    for passphrase in passphrases:
        passphrase = [frozenset(s) for s in passphrase]
        if len(set(passphrase)) == len(passphrase):
            valid += 1
    return valid

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

