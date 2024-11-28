import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[1].input_data
data = input_data

data = data.split("\n")

class Program:
    def __init__(self, id: int):
        self.regs = {chr(i + ord('a')): 0 for i in range(26)}
        self.regs['p'] = id
        self.pc = 0
        self.queue = [] #recieve queue
        self.dual = None
        self.wait = False
        self.sent = 0

    def duet(self, other):
        self.dual = other
    
    def compute(self):
        if 0 <= self.pc < len(code):
            cmd, x, y = code[self.pc]
            match cmd:
                case "snd":
                    if isinstance(x, str):
                        x = self.regs[x]
                    self.dual.queue.append(x)
                    self.sent += 1
                case "rcv":
                    if self.queue:
                        self.regs[x] = self.queue.pop(0)
                        self.wait = False
                    else:
                        self.pc -= 1
                        self.wait = True
                case "set":
                    if isinstance(y, str):
                        y = self.regs[y]
                    self.regs[x] = y
                case "add":
                    if isinstance(y, str):
                        y = self.regs[y]
                    self.regs[x] += y
                case "mul":
                    if isinstance(y, str):
                        y = self.regs[y]
                    self.regs[x] *= y
                case "mod":
                    if isinstance(y, str):
                        y = self.regs[y]
                    self.regs[x] %= y
                case "jgz":
                    if isinstance(x, str):
                        x = self.regs[x]
                    if isinstance(y, str):
                        y = self.regs[y] 
                    if x > 0:
                        self.pc += y - 1
            self.pc += 1
        return self.wait, 0 <= self.pc < len(code)
        
code = []
for line in data:
    line: list[str] = line.split()
    cmd = line[0]
    x = line[1]
    if len(line) > 2:
        y = line[2]
    match cmd:
        case "snd" | "rcv":
            if x.isdigit() or x[1:].isdigit():
                x = int(x)
            y = None
        case "set" | "add" | "mul" | "mod":
            if y.isdigit() or y[1:].isdigit():
                y = int(y)
        case "jgz":
            if x.isdigit() or x[1:].isdigit():
                x = int(x)
            if y.isdigit() or y[1:].isdigit():
                y = int(y)
    code.append((cmd, x, y))


def solution_a():
    regs = {chr(i + ord('a')): 0 for i in range(26)}
    sound = 0
    pc = 0
    while 0 <= pc < len(code):
        cmd, x, y = code[pc]
        match cmd:
            case "snd":
                if isinstance(x, str):
                    x = regs[x]
                sound = x
            case "rcv":
                if isinstance(x, str):
                    x = regs[x]
                if x:
                    return sound
            case "set":
                if isinstance(y, str):
                    y = regs[y]
                regs[x] = y
            case "add":
                if isinstance(y, str):
                    y = regs[y]
                regs[x] += y
            case "mul":
                if isinstance(y, str):
                    y = regs[y]
                regs[x] *= y
            case "mod":
                if isinstance(y, str):
                    y = regs[y]
                regs[x] %= y
            case "jgz":
                if isinstance(x, str):
                    x = regs[x]
                if isinstance(y, str):
                    y = regs[y] 
                if x > 0:
                    pc += y - 1
        pc += 1
    return -1


def solution_b():
    a, b = Program(0), Program(1)
    a.duet(b), b.duet(a)
    both_wait, both_in_range = False, True
    while not both_wait and both_in_range:
        a_wait, a_in_range = a.compute()
        b_wait, b_in_range = b.compute()
        both_wait = a_wait and b_wait
        both_in_range = a_in_range and b_in_range
    return b.sent
    



print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

