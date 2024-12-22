import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
from heapq import heappush, heappop
puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

towels, patterns = data.split("\n\n")

towels = set(t for t in towels.split(", "))

shortest_t = len(min(towels, key=len))
patterns = tuple(p for p in patterns.split())

def solution_a():
    valid = 0
    for pattern in patterns:
        tried = set()
        s = [0]
        while s:
            p = s.pop()
            tried.add(p)
            if p == len(pattern):
                valid += 1
                break
            for i in range(shortest_t + p, len(pattern) + 1):
                if pattern[p:i] in towels and i not in tried: #maybe and i not in s?
                    s.append(i)
    return valid

def solution_b():
    valid = 0
    for pattern in patterns:
        tried = {0: 1}
        q = [0]
        while q:
            p = heappop(q)
            if p == len(pattern):
                valid += tried[p]
                break
            for i in range(shortest_t + p, len(pattern) + 1):
                if pattern[p:i] in towels: #maybe and i not in s?
                    if i not in q:
                        heappush(q, i)
                    if i not in tried:
                        tried[i] = 0
                    tried[i] += tried[p]
            
    return valid



print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

