import sys
from hashlib import md5
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data


def solution_a():
    password = ""
    i = 0
    while len(password) < 8:
        s = md5((data + str(i)).encode()).hexdigest()
        if s[:5] == "00000":
            password += s[5]
        i += 1
    return password

def solution_b():
    password = [0 for i in range(8)]
    i = 0
    while sum([1 for i in password if isinstance(i, int)]) > 0:
        s = md5((data + str(i)).encode()).hexdigest()
        if s[:5] == "00000" and int(s[5], 16) < 8 and isinstance(password[int(s[5])], int):
            password[int(s[5])] = s[6]
        i += 1
    return "".join(password)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

