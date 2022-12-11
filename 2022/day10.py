from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=10)

with open('2022\\examples\\day10example.txt', 'r') as f:
    data = f.read()
data = puzzle.input_data
#data = "noop\naddx 3\naddx -5"

data = [line.split(" ") for line in data.split("\n")]

x = 1
cycle = 0
crt = [[' '] for i in range(240)]

signal_strength = 0

def check_strength():
    crt[cycle - 1] = '#' if x - 1 <= (cycle - 1) % 40 <= x + 1 else ' '
    if (cycle - 20) % 40 == 0:
        return cycle * x
    return 0

def print_crt(crt):
    for i, pixel in enumerate(crt):
        if i % 40 == 0:
            print("\n", end="")
        print(pixel, end="")
    print()

for command in data:
    match command[0]:
        case 'addx':
            cycle += 1
            signal_strength += check_strength()
            cycle += 1
            signal_strength += check_strength()
            x += int(command[1])
        case 'noop':
            cycle += 1
            signal_strength += check_strength()



print(f"a: {signal_strength}")
puzzle.answer_a = signal_strength


print(f"b: EKRHEPUZ", end="")
print_crt(crt)
puzzle.answer_b = "EKRHEPUZ"



