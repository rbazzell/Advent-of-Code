import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n\n")

class Board:
    def __init__(self, b: str):
        self.marked = [[0 for _ in range(5)] for _ in range(5)]
        self.values = tuple(tuple(int(x) for x in line.split()) for line in b.split("\n"))
        self.locs = dict()
        for i in range(5):
            for j in range(5):
                self.locs[self.values[i][j]] = (i, j)
        self.bingo = False

    def __repr__(self):
        return aocu.grid_str(self.values, spaces=3)
    
    def has_bingo(self) -> bool:
        bingo = False
        for line in self.marked:
            bingo = bingo or sum(line) == 5
        for line in zip(*self.marked):
            bingo = bingo or sum(line) == 5
        self.bingo = bingo
        return bingo

    def score(self, call) -> int:
        unmarked_sum = 0
        for i in range(5):
            for j in range(5):
                if self.marked[i][j] == 0:
                    unmarked_sum += self.values[i][j]
        return unmarked_sum * call
    
    def mark(self, call) -> bool:
        if call in self.locs:
            i, j = self.locs[call]
            self.marked[i][j] = 1
            return True
        return False

calls = tuple(int(x) for x in data[0].split(","))
boards = [Board(x) for x in data[1:]]
        
def solution_a():
    for call in calls:
        for board in boards:
            if board.mark(call) and board.has_bingo():
                return board.score(call)
    return -1

def solution_b():
    bingos = 0
    for call in calls:
        for board in boards:
            if not board.bingo and board.mark(call) and board.has_bingo():
                bingos += 1
            if bingos == len(boards):
                return board.score(call)
    return -1

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

