import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = [line.split(": ") for line in data.split("\n")]
scanners = {int(line[0]): int(line[1]) for line in data}

def solution_a():
    severity = 0
    for i in range(max(scanners.keys()) + 1):
        if scanners.get(i) and i % (2 * scanners[i] - 2) == 0:
            severity += i * scanners[i]
    return severity

def solution_b():
    offset = 0
    caught = True
    while caught:
        caught = False
        for i in range(offset, max(scanners.keys()) + offset + 1):
            if scanners.get(i - offset) and i % (2 * scanners[i - offset] - 2) == 0:
                offset += 1
                caught = True
                break
    return offset


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

