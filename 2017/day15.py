import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

class Generator:
    def __init__(self, start: int, factor: int, critera: int=1):
        self.v = start
        self.f = factor
        self.c = critera

    def next(self):
        self.v = (self.v * self.f) % 2147483647
        while self.v % self.c != 0:
            self.v = (self.v * self.f) % 2147483647
        return self.v



def solution_a():
    iters = 40000000
    judge_count = 0
    A, B = Generator(int(data[0].split()[-1]), 16807), Generator(int(data[1].split()[-1]), 48271)
    for i in range(iters):
        a, b = A.next() & 0xFFFF, B.next() & 0xFFFF
        if a == b:
            judge_count += 1
    return judge_count
    

def solution_b():
    iters = 5000000
    judge_count = 0
    A, B = Generator(int(data[0].split()[-1]), 16807, 4), Generator(int(data[1].split()[-1]), 48271, 8)
    for i in range(iters):
        a, b = A.next() & 0xFFFF, B.next() & 0xFFFF
        if a == b:
            judge_count += 1
    return judge_count

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

