import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = [int(x) for x in data.split()]

class Bank:
    def __init__(self, blocks: list[int]):
        self.banks = {i: x for i, x in enumerate(blocks)}

    def __getitem__(self, i):
        return self.banks[i]
    
    def __hash__(self):
        return hash((*self.banks.items(),))
    
    def __repr__(self):
        return " ".join([str(x) for x in self.banks.values()])

    def do_cycle(self):
        bank = max(self.banks, key=self.banks.get)
        blocks = self.banks[bank]
        self.banks[bank] = 0
        for b in self.banks.keys():
            self.banks[b] += blocks // len(self.banks)
        for b in range(bank + 1, blocks % len(self.banks) + bank + 1):
            self.banks[b % len(self.banks)] += 1

    def copy(self):
        bank = Bank([])
        bank.banks = self.banks.copy()
        
def solution_a():
    bank = Bank(data)
    visited = set()
    cycles = 0
    while bank not in visited:
        visited.add(bank)
        bank.do_cycle()
        cycles += 1
    return cycles

def solution_b():
    bank = Bank(data)
    visited = dict()
    cycles = 0
    while not visited.get(frozenset({bank})):
        visited[frozenset({bank})] = cycles
        bank.do_cycle()
        cycles += 1
    return cycles - visited[frozenset({bank})]

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

