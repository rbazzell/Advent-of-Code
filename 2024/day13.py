import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n\n")

machines = list()
for machine in data:
    machine = machine.split("\n")
    a = machine[0].split()
    b = machine[1].split()
    prize = machine[2].split()

    a = (int(a[2][2:-1]), int(a[3][2:]))
    b = (int(b[2][2:-1]), int(b[3][2:]))
    prize = [int(prize[1][2:-1]), int(prize[2][2:])]

    machines.append((a, b, prize))


def solution_a():
    tokens = 0
    for a, b, prize in machines:
        #matrix multiplication to solve system of equations
        #a=a[0], b=b[0], c=a[1], d=b[1]
        det = a[0]*b[1] - b[0]*a[1]
        a_tokens =  b[1]*prize[0] - b[0]*prize[1]
        b_tokens = -a[1]*prize[0] + a[0]*prize[1]
        if a_tokens % det == 0 and b_tokens % det == 0:
            a_tokens //= det
            b_tokens //= det
            tokens += 3*a_tokens + b_tokens
    return tokens


def solution_b():
    tokens = 0
    for a, b, prize in machines:
        #matrix multiplication to solve system of equations
        #a=a[0], b=b[0], c=a[1], d=b[1]
        prize[0] += 10000000000000
        prize[1] += 10000000000000
        det = a[0]*b[1] - b[0]*a[1]
        a_tokens =  b[1]*prize[0] - b[0]*prize[1]
        b_tokens = -a[1]*prize[0] + a[0]*prize[1]
        if a_tokens % det == 0 and b_tokens % det == 0:
            a_tokens //= det
            b_tokens //= det
            tokens += 3*a_tokens + b_tokens
    return tokens

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

