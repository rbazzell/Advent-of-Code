import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

ranges = [x.split(" ")[0].split("-") for x in data]
letter_req = [x.split(" ")[1][0] for x in data]
password = [x.split(" ")[2] for x in data]

def solution_a(data):
    valid_passwords = 0
    for i in range(len(ranges)):
        valid_count = password[i].count(letter_req[i])
        range_min = int(ranges[i][0])
        range_max = int(ranges[i][1])
        if valid_count >= range_min and valid_count <= range_max:
            valid_passwords += 1
    return valid_passwords

def solution_b(data):
    valid_passwords = 0
    for i in range(len(ranges)):
        range_min = int(ranges[i][0])
        range_max = int(ranges[i][1])
        position_a = password[i][range_min - 1]
        position_b = password[i][range_max - 1]

        if (position_a is letter_req[i]) ^ (position_b is letter_req[i]):
            valid_passwords += 1
    return valid_passwords

print(solution_b(data))
#puzzle.answer_a = solution_a(data)
puzzle.answer_b = solution_b(data)

