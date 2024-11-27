import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data, programs = examples[0].input_data, "abcde"
data, programs = input_data, "abcdefghijklmnop"

data = data.split(",")
instructions = []
for inst in data:
    command = inst[0]
    match command:
        case "s":
            arg1 = int(inst[1:])
            arg2 = None
        case "x":
            slash = inst.find("/")
            arg1 = int(inst[1:slash])
            arg2 = int(inst[slash+1:])
        case "p":
            slash = inst.find("/")
            arg1 = inst[1:slash]
            arg2 = inst[slash+1:]
    instructions.append((command, arg1, arg2))

def dance(prgms: list[str]):
    for command, arg1, arg2 in instructions:
        match command:
            case "s":
                prgms = prgms[-arg1:] + prgms[:-arg1]
            case "x":
                prgms[arg1], prgms[arg2] = prgms[arg2], prgms[arg1]
            case "p":
                a, b = prgms.index(arg1), prgms.index(arg2)
                prgms[a], prgms[b] = prgms[b], prgms[a]
    return prgms


def solution_a():
    prgms: list[str] = list(programs)
    return "".join(dance(prgms))


def solution_b():
    times = 1
    prgms: list[str] = dance(list(programs))
    while prgms != list(programs):
        times += 1
        prgms = dance(prgms)
    for _ in range((1000000000 - 1) % times):
        prgms = dance(prgms)
    return "".join(dance(prgms))
    

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

