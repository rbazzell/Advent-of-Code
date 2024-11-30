import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

components = [tuple([int(x) for x in line.split("/")]) for line in data.split("\n")]


def solution_a():
    queue = list()
    visited = set()
    for component in components:
        if component[0] == 0:
            queue.append((component[1], {component}, sum(component)))
            visited.add(frozenset({component}))
        elif component[1] == 0:
            queue.append((component[0], {component}, sum(component)))
            visited.add(frozenset({component}))
    max_strength = 0
    while queue:
        port, bridge, strength = queue.pop(0)
        max_strength = max(strength, max_strength)
        for component in components:
            if component not in bridge and frozenset(bridge | {component}) not in visited:
                if component[0] == port:
                    queue.append((component[1], bridge | {component}, strength + sum(component)))
                    visited.add(frozenset(bridge | {component}))
                elif component[1] == port:
                    queue.append((component[0], bridge | {component}, strength + sum(component)))
                    visited.add(frozenset(bridge | {component}))
    return max_strength
    

def solution_b():
    queue = list()
    visited = set()
    for component in components:
        if component[0] == 0:
            queue.append((component[1], {component}, sum(component)))
            visited.add(frozenset({component}))
        elif component[1] == 0:
            queue.append((component[0], {component}, sum(component)))
            visited.add(frozenset({component}))
    max_strength = 0
    max_length = 1
    while queue:
        port, bridge, strength = queue.pop(0)
        if len(bridge) == max_length:
            max_strength = max(strength, max_strength)
        elif len(bridge) > max_length:
            max_length = len(bridge)
            max_strength = strength
        for component in components:
            if component not in bridge and frozenset(bridge | {component}) not in visited:
                if component[0] == port:
                    queue.append((component[1], bridge | {component}, strength + sum(component)))
                    visited.add(frozenset(bridge | {component}))
                elif component[1] == port:
                    queue.append((component[0], bridge | {component}, strength + sum(component)))
                    visited.add(frozenset(bridge | {component}))
    return max_strength

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

