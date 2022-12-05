from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=5)
#data = puzzle.example_data
data = puzzle.input_data

def print_stacks(stacks):
    text = " "
    for j in range(len(stacks)):
        text += f"{j + 1}   "
    x = len(max(stacks, key=len))
    for i in range(x):
        line = ""
        for stack in stacks:
            if i < len(stack):
                line += f"[{stack[i]}] "
            else:
                line += "    "
        text = line + "\n" + text
    return text

towers = data.split("\n\n")[0].split("\n")[:-1]
commands = data.split("\n\n")[1].split("\n")
stacks_a = [[] for i in range((len(towers[0]) + 1) // 4)]
stacks_b = [[] for i in range((len(towers[0]) + 1) // 4)]
for line in towers:
    for i in range(len(stacks_a)):
        if line[1 + i * 4] != " ":
            stacks_a[i].insert(0, line[1 + i*4])
            stacks_b[i].insert(0, line[1 + i*4])

for command in commands: #5:6 = quantity, -6 = from, -1 = destination
    o_len = len(stacks_b[int(command[-6]) - 1])
    for crate in range(int(command[5:7])):
        stacks_a[int(command[-1]) - 1].append(stacks_a[int(command[-6]) - 1].pop())
        stacks_b[int(command[-1]) - 1].append(stacks_b[int(command[-6]) - 1].pop(o_len - int(command[5:7])))
    #print(f"{print_stacks(stacks_b)}")

tops_a = ""
tops_b = ""

for stack in stacks_a:
    tops_a += stack[-1]
for stack in stacks_b:
    tops_b += stack[-1]

print(f"a: {tops_a}")
#puzzle.answer_a = tops

print(f"b: {tops_b}")
puzzle.answer_b = tops_b
