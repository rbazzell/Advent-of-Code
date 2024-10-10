import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(14, 2020)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = "mask = 000000000000000000000000000000X1001X\nmem[42] = 100\nmask = 00000000000000000000000000000000X0XX\nmem[26] = 1"
data = input_data

data = data.split("\n")

commands = list()
for line in data:
    if line[0:4] == "mask":
        commands.append(["mask", line[7:]])
    elif line[0:4] == "mem[":
        commands.append(["mem", int(line.split("]")[0][4:]), int(line.split(" = ")[1])])

def solution_a():
    memory = dict()
    for cmd in commands:
        match cmd[0]:
            case "mask":
                one_mask = int(cmd[1].replace("X", "0"), 2) #this one gets ORed
                zero_mask = int(cmd[1].replace("X", "1"), 2) #this one get ANDED
            case "mem":
                value = cmd[2]
                value |= one_mask
                value &= zero_mask
                memory[cmd[1]] = value

    return sum(memory.values())

                

def solution_b():
    memory = dict()
    for cmd in commands:
        match cmd[0]:
            case "mask":
                mask = cmd[1]
            case "mem":
                for m in all_possibilities(cover(bit36(cmd[1]), mask)):
                    memory[m] = cmd[2]

    return sum(memory.values())

def bit36(num: int) -> str:
    num = format(num, 'b')
    return (36 - len(num)) * "0" + num

def cover(num: str, mask: str) -> str:
    r = ""
    for n, m in zip(num, mask):
        if m == "0":
            r += n
        if m == "1":
            r += "1"
        if m == "X":
            r += "X"
    return r

def all_possibilities(mask: str) -> list[int]:
    masks = list()
    i = mask.find("X")
    if i == -1:
        masks.append(int(mask, 2))
    else:
        masks.extend(all_possibilities(mask[:i] + "0" + mask[i+1:]))
        masks.extend(all_possibilities(mask[:i] + "1" + mask[i+1:]))
    return masks

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

