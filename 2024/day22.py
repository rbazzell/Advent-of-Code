import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
from time import time_ns

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = """1
2
3
2024"""
data = input_data

secrets = [int(x) for x in data.split("\n")]

def new_secret(s: int) -> int:
    s ^= s << 6 & 0xFFFFFF
    s ^= s >> 5 & 0xFFFFFF
    return s ^ s << 11 & 0xFFFFFF

def solution_a():
    total = 0
    for s in secrets:
        for _ in range(2000):
            s = new_secret(s)
        total += s
    return total

def solution_b():
    sequences = dict()
    for s in secrets:
        prev = s % 10
        diffs = (None, None, None, None)
        sequence = dict()
        for _ in range(2000):
            s = new_secret(s)
            diffs = (*diffs[1:], s%10 - prev)
            if None not in diffs and diffs not in sequence:
                sequence[diffs] = s%10
            prev = s % 10
        for s, v in sequence.items():
            if s not in sequences:
                sequences[s] = 0
            sequences[s] += v
    return max(sequences.values())
            



print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

