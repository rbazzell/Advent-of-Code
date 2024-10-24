import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[1].input_data
data = input_data

def increase_password(password:str):
    ascii_code = [ord(x) for x in password]

    increment = True
    for i in range(len(ascii_code) - 1, -1, -1):
        if increment:
            ascii_code[i] += 1
        if ascii_code[i] in (ord('i'),ord('o'),ord('l')):
            ascii_code[i] += 1
            for j in range(i+1, len(ascii_code)):
                ascii_code[j] = ord('a')
        if ascii_code[i] > ord('z'):
            ascii_code[i] -= 26
        else:
            increment = False
    return "".join([chr(x) for x in ascii_code])


def solution_a():
    password = data
    abcs = [f"{chr(x)}{chr(x+1)}{chr(x+2)}" for x in range(ord('a'), ord('z') - 1)]
    a_z_2 = [f"{chr(x)}{chr(x)}" for x in range(ord('a'), ord('z') + 1)]

    increasing_straights = 0
    iol_count = 1
    repeats = 0
    while increasing_straights < 1 or iol_count > 0 or repeats < 2:
        password = increase_password(password)
        increasing_straights = sum([password.count(x) for x in abcs])
        iol_count = sum([password.count(x) for x in ('i','o','l')])
        repeats = sum([password.count(x) for x in a_z_2])
    return password


def solution_b():
    global data
    data = solution_a()
    return solution_a()

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

