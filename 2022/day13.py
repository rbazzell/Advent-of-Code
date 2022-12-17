from aocd.models import Puzzle
from functools import cmp_to_key
import os, ast
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=13)
data = puzzle.example_data
data = puzzle.input_data
data = [line.split("\n") for line in data.split("\n\n")]

for packet in data:
    packet[0] = ast.literal_eval(packet[0])
    packet[1] = ast.literal_eval(packet[1])

def compare_types(a, b) -> int: # -1 means wrong order, 0 means keep going, 1 means right order
        if isinstance(a, int) and isinstance(b, int):
            if a == b:
                return 0
            elif a < b:
                return 1
            else:
                return -1
        elif isinstance(a, list) and isinstance(b, list):
            for i in range(max(len(a), len(b))):
                if i >= len(a):
                    return 1
                elif i >= len(b):
                    return -1
                match compare_types(a[i], b[i]):
                    case -1:
                        return -1
                    case 1:
                        return 1
            return 0
        elif isinstance(a, int) and isinstance(b, list):
            a = [a]
            return compare_types(a, b)
        elif isinstance(a, list) and isinstance(b, int):
            b = [b]
            return compare_types(a, b)


packets = list()
ans_a = 0
for j, packet in enumerate(data):
    if compare_types(packet[0], packet[1])  == 1:
        ans_a += (1 + j)
    packets.append(packet[0])
    packets.append(packet[1])
if [[2]] not in packets:
    packets.append([[2]])
if [[6]] not in packets:
    packets.append([[6]])

packets.sort(key=cmp_to_key(compare_types), reverse=True)

ans_b = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print(f"a: {ans_a}")
#puzzle.answer_a = ans_a

print(f"b: {ans_b}")
puzzle.answer_b = ans_b