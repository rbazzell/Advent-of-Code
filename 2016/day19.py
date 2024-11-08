import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = int(data)

class terint:
    def __init__(self, n: int):
        self.n = n
    def __lshift__(self, value: int):
        return terint(self.n * (3**value))
    def __rshift__(self, value: int):
        return terint(self.n // (3**value))
    def trit_length(self) -> int:
        trits = 0
        n = self.n
        while n > 0:
            trits += 1
            n //= 3
        return trits
    def mst(self):
        n = self.n
        while n > 2:
            n //= 3
        return n
    def __sub__(self, value: int) -> int:
        return self.n - value
    



def solution_a():
    #Formula created using the Josephus Problem
    # as featured on the Numberphile YouTube Channel
    return (data << 1) - (1 << data.bit_length()) + 1

def solution_b():
    #formula derived using a similar process to the one above
    #but done manually on scratch paper
    winner = 0 
    tri = terint(data)
    if tri.mst() == 2:
        factor = 3**(tri.trit_length()-1)
        winner += tri - factor
        tri = terint(tri - factor)
    factor = tri - 3**(tri.trit_length()-1)
    if factor == 0:
        factor = tri.n
    winner += factor

    

    return winner

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

