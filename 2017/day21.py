import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data: list[str] = data.split("\n")
start = [['.','#','.'], ['.','.','#'], ['#','#','#']]
enhancements = {}
for line in data:
    key, value = line.split(" => ")
    key = tuple(tuple(x) for x in key.split("/"))
    value = [list(x) for x in value.split("/")]
    enhancements[key] = value
    for flip in range(2):
        for rotation in range(4):
            enhancements[key] = value
            key = tuple(zip(*key[::-1]))
        key = key[::-1]

def solution_a():
    art = start.copy()
    for _ in range(5):
        if len(art) % 2 == 0:
            div = 2
            l = len(art) // 2 * 3
        else:
            div = 3
            l = len(art) // 3 * 4
        n_art = [["" for _ in range(l)] for _ in range(l)]
        for r in range(0, len(art), div):
            for c in range(0, len(art[r]), div):
                segment = tuple(tuple(x[c:c+div]) for x in art[r:r+div])
                nr, nc = r // div * (div + 1), c // div * (div + 1)
                for dr in range(div + 1):
                    for dc in range(div + 1):
                        n_art[nr+dr][nc+dc] = enhancements[segment][dr][dc]
        art = n_art
    return sum([x.count("#") for x in art])

def solution_b():
    art = start.copy()
    for _ in range(18):
        if len(art) % 2 == 0:
            div = 2
            l = len(art) // 2 * 3
        else:
            div = 3
            l = len(art) // 3 * 4
        n_art = [["" for _ in range(l)] for _ in range(l)]
        for r in range(0, len(art), div):
            for c in range(0, len(art[r]), div):
                segment = tuple(tuple(x[c:c+div]) for x in art[r:r+div])
                nr, nc = r // div * (div + 1), c // div * (div + 1)
                for dr in range(div + 1):
                    for dc in range(div + 1):
                        n_art[nr+dr][nc+dc] = enhancements[segment][dr][dc]
        art = n_art
    return sum([x.count("#") for x in art])


print(solution_a())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

