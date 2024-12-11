import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
#data = input_data

diagnostics = tuple(tuple(int(y) for y in x) for x in data.split("\n"))
bits = len(data.split("\n")[0])


def solution_a():
    gamma = int("".join("1" if sum(x) > len(diagnostics) // 2 else "0" for x in zip(*diagnostics)), 2)
    epsilon = (1 << bits) - 1 - gamma #bitwise not
    return gamma * epsilon

def solution_b():
    oxygen, carbon = 0, 0
    o2_con, co2_con = diagnostics, diagnostics
    for b in range(bits):
        o2_maj = 1 if sum(report[b] for report in o2_con) >= len(o2_con) // 2 + len(o2_con) % 2 else 0
        co2_min = 1 if sum(report[b] for report in co2_con) < len(co2_con) // 2 + len(co2_con) % 2 else 0

        o2_con = tuple(report for report in o2_con if report[b] == o2_maj)
        co2_con = tuple(report for report in co2_con if report[b] == co2_min)

        if not oxygen and len(o2_con) == 1:
            oxygen = int("".join("1" if o2_con[0][b] else "0" for b in range(bits)), 2)
        if not carbon and len(co2_con) == 1:
            carbon = int("".join("1" if co2_con[0][b] else "0" for b in range(bits)), 2)
        if oxygen and carbon:
            break
    return oxygen * carbon



print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

