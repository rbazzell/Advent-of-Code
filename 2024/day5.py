import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

ordering_rules, productions = tuple(line.split("\n") for line in data.split("\n\n"))

rev_order_rules: dict[int, set[int]] = dict()
for line in ordering_rules:
    before, after = tuple(int(x) for x in line.split("|"))
    if after not in rev_order_rules:
        rev_order_rules[after] = set()
    rev_order_rules[after].add(before)

productions = [[int(x) for x in line.split(",")] for line in productions]

def solution_a() -> int:
    total = 0
    for p in productions:
        if ordered(p):
            total += p[len(p) // 2]
    return total

def ordered(p) -> bool:
    so_far = set()
    ps = set(p)
    for n in p:
        so_far.add(n)
        if n in rev_order_rules and not rev_order_rules[n] & ps <= so_far:
            return False
    return True

def find_unorder(p) -> tuple[int, int]:
    so_far = set()
    ps = set(p)
    for n in p:
        so_far.add(n)
        if n in rev_order_rules and not rev_order_rules[n] & ps <= so_far:
            return n, ((rev_order_rules[n] & ps) - so_far).pop()
    return True

def solution_b() -> int:
    #find unordered ones
    fully_ordered = list()
    for p in productions:
        while not ordered(p):
            n, m = find_unorder(p)
            i, j = sorted((p.index(n), p.index(m)))
            p = p[:i] + [p[j]] + p[i+1:j] + [p[i]] + p[j+1:]
        fully_ordered.append(p)
    
    total = sum([p[len(p)//2] for p in fully_ordered]) - solution_a()
    return total

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

