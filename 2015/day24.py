import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
data = [int(x) for x in data]

def find_groups(elements: list[int], target: int):
    #ChatGPT helped me produce this from a less efficient version I created
    #Same worst case asymptotic performance
    #Better average case performance b/c it allows us to cut off invalid groups higher up
    #                                    on the recursion tree before they explode
    #It also cleaned up the formatting a bit, but the corpse of my algorithm is still present
    elements.sort(reverse=True)
    groups = set()

    def backtrack(start, group):
        if sum(group) == target:
            groups.add(frozenset(group))
            return
        if sum(group) > target:
            return
        for i in range(start, len(elements)):
            backtrack(i+1, group + [elements[i]])

    backtrack(0, [])
    return groups




def product(L : list[int]):
    prod = 1
    for e in L:
        prod *= e
    return prod

def solution_a():
    best_group = data.copy()
    for group in list(find_groups(data, sum(data) // 3)):
        if len(group) < len(best_group):
            best_group = group
        if len(group) == len(best_group) and product(group) < product(best_group):
            best_group = group
    return product(best_group)


def solution_b():
    best_group = data.copy()
    for group in list(find_groups(data, sum(data) // 4)):
        if len(group) < len(best_group):
            best_group = group
        if len(group) == len(best_group) and product(group) < product(best_group):
            best_group = group
    return product(best_group)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

