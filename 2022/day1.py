from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"

puzzle = Puzzle(year=2022, day=1)
#data = puzzle.example_data
data = puzzle.input_data

data = [[int(y) for y in x.split("\n")] for x in data.split("\n\n")]

elfs = [sum(x) for x in data]
elfs.sort(reverse=True)

print(f"a: {elfs[0]}")
#puzzle.answer_a = elfs[0]

print(f"b: {sum(elfs[0:3])}")
puzzle.answer_b = sum(elfs[0:3])