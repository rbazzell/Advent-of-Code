import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

network: tuple[tuple[str]] = tuple(tuple(line.split("-")) for line in data.split("\n"))
connections: dict[str, set[str]] = dict()
for pc1, pc2 in network:
    if pc1 not in connections:
        connections[pc1] = set()
    if pc2 not in connections:
        connections[pc2] = set()
    connections[pc1].add(pc2)
    connections[pc2].add(pc1)

def three_cliques(connections):
    cliques = set()
    for pc1 in connections.keys():
        for pc2 in connections[pc1]:
            for pc3 in connections[pc2]:
                if pc3 not in (pc1, pc2) and pc3 in connections[pc1]:
                    cliques.add(frozenset((pc1, pc2, pc3)))
    return cliques

def solution_a():
    lan_parties = three_cliques(connections)
    return len(set(frozenset({pc1, pc2, pc3}) for pc1, pc2, pc3 in lan_parties if 't' in (pc1[0], pc2[0], pc3[0])))


def solution_b():
    cliques: set[frozenset[str]] = three_cliques(connections)
    while len(cliques) > 1:
        new_cliques = set()
        for clique in cliques:
            clique = set(clique)
            pc1 = clique.pop()

            for pc2 in connections[pc1]:
                cliquable = True
                for pc in clique:
                    if pc2 not in connections[pc]:
                        cliquable = False
                        break
                if cliquable:
                    new_cliques.add(frozenset(clique | {pc1, pc2}))
        cliques = new_cliques
    
    lan_party = sorted(cliques.pop())
    return ",".join(lan_party)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

