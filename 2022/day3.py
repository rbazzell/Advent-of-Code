from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=3)
#data = puzzle.example_data
data = puzzle.input_data

data = data.split("\n")

def priority_value(char):
    if char.isupper():
        return ord(char) - 38
    return ord(char) - 96

priority = 0
for rucksack in data:
    for item in rucksack[:len(rucksack) // 2]:
        if item in rucksack[len(rucksack) // 2:]:
            priority += priority_value(item)
            break

badges = 0
bags = iter(data)
for sack1, sack2, sack3 in zip(bags, bags, bags):
    for item in sack1:
        if item in sack2 and item in sack3:
            badges += priority_value(item)
            break

print(f"a: {priority}")
#puzzle.answer_a = priority

print(f"b: {badges}")
puzzle.answer_b = badges