import sys
from math import log10
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = "125 17"
data = input_data

start_stones = dict()
for line in data.split():
    if int(line) not in start_stones:
        start_stones[int(line)] = 0
    start_stones[int(line)] += 1


def solution_a():
    stones = start_stones
    blinks = 25
    for _ in range(blinks):
        new_stones = dict()
        for stone, num in stones.items():
            slots = []
            if stone == 0:
                slots = [1]
            else:
                digits = (int(log10(stone)) + 1)
                if digits % 2 == 0:
                    reduction = (10 ** (digits // 2))
                    slots = [stone // reduction, stone % reduction]
                else:
                    slots = [stone * 2024]
            for slot in slots:
                if slot not in new_stones:
                    new_stones[slot] = 0
                new_stones[slot] += num
        stones = new_stones
    return sum(new_stones.values()) 


def solution_b():
    stones = start_stones
    blinks = 75
    for _ in range(blinks):
        new_stones = dict()
        for stone, num in stones.items():
            slots = []
            if stone == 0:
                slots = [1]
            else:
                digits = (int(log10(stone)) + 1)
                if digits % 2 == 0:
                    reduction = (10 ** (digits // 2))
                    slots = [stone // reduction, stone % reduction]
                else:
                    slots = [stone * 2024]
            for slot in slots:
                if slot not in new_stones:
                    new_stones[slot] = 0
                new_stones[slot] += num
        stones = new_stones
    return sum(new_stones.values()) 

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

