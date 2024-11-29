import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

#data = examples[0].input_data
data = input_data

data = data.split("\n")

code = []
for line in data:
    line: list[str] = line.split()
    cmd = line[0]
    x = line[1]
    if len(line) > 2:
        y = line[2]
    match cmd:
        case "set" | "sub" | "mul":
            if y.isdigit() or y[1:].isdigit():
                y = int(y)
        case "jnz":
            if x.isdigit() or x[1:].isdigit():
                x = int(x)
            if y.isdigit() or y[1:].isdigit():
                y = int(y)
    code.append((cmd, x, y))

def solution_a():
    regs = {chr(i + ord('a')): 0 for i in range(8)}
    muls = 0
    pc = 0
    while 0 <= pc < len(code):
        cmd, x, y = code[pc]
        match cmd:
            case "set":
                if isinstance(y, str):
                    y = regs[y]
                regs[x] = y
            case "sub":
                if isinstance(y, str):
                    y = regs[y]
                regs[x] -= y
            case "mul":
                if isinstance(y, str):
                    y = regs[y]
                regs[x] *= y
                muls += 1
            case "jnz":
                if isinstance(x, str):
                    x = regs[x]
                if isinstance(y, str):
                    y = regs[y] 
                if x != 0:
                    pc += y - 1
        pc += 1
    return muls


def solution_b():
    h = 0
    b = 108400
    c = 125400

    for b in range(b, c + 1, 17):
        if not prime(b):
            h += 1
    return h

def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i==0:
            return False
    return True

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

