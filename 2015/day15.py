import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

class Cookie:
    def __init__(self, description:str):
        description = description.split(" ")
        self.name = description[1][:-1]
        self.capacity = int(description[2][:-1])
        self.durability = int(description[4][:-1])
        self.flavor = int(description[6][:-1])
        self.texture = int(description[8][:-1])
        self.calories = int(description[10])

cookies = [Cookie(line) for line in data]

def sum_to_n(n:int, size: int, limit: int=None):
    if size == 1:
        yield [n]
        return
    if limit == None:
        limit = n
    for i in range(0, min(n, n - size + 1) + 1):
        for tail in sum_to_n(n-i, size-1, i):
            yield [i] + tail


def test_combo(n, check_calories=False):
    capacity = sum([cookies[i].capacity * n[i] for i in range(len(n))])
    durability = sum([cookies[i].durability * n[i] for i in range(len(n))])
    flavor = sum([cookies[i].flavor * n[i] for i in range(len(n))])
    texture = sum([cookies[i].texture * n[i] for i in range(len(n))])
    if check_calories:
        calories = sum([cookies[i].calories * n[i] for i in range(len(n))])
    else:
        calories = 500
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0 or calories != 500:
        return 0
    return capacity * durability * flavor * texture

def solution_a():
    best_cookie = 0
    for hundred in sum_to_n(100, len(cookies)):
        best_cookie = max(best_cookie, test_combo(hundred))
    return best_cookie


def solution_b():
    best_cookie = 0
    for hundred in sum_to_n(100, len(cookies)):
        best_cookie = max(best_cookie, test_combo(hundred, True))
    return best_cookie

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

