import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
card_key = int(data[0])
door_key = int(data[1])


def solution_a():

    #trial and error to obtain loop sizes
    card_loop = 0
    door_loop = 0
    val = 1
    secret_number = 7
    loop = 0
    while not card_loop or not door_loop:
        loop += 1
        val = (val * secret_number) % 20201227
        if val == card_key:
            card_loop = loop
        if val == door_key:
            door_loop = loop

    val = 1
    secret_number = door_key
    for loop in range(card_loop):
        val = (val * secret_number) % 20201227
    return val
        



def solution_b():
    pass

print(solution_a())
puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

