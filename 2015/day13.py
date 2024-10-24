import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")




manifest: dict[str, dict[str, int]] = dict()

for line in data:
    line = line.split(" ")
    id = line[0]
    dest = line[-1][:-1]
    happiness = -int(line[3]) if line[2] == "lose" else int(line[3])

    if manifest.get(id) == None:
        manifest[id] = dict()
    manifest[id][dest] = happiness

def path(id: str, visited: list[str]):
    weights = []
    for dest in manifest[id].keys():
        if len(visited) == len(manifest) - 1:
            weight = manifest[id][visited[0]] + manifest[visited[0]][id]
            weights = [weight]
            break
        elif dest not in visited:
            weight = manifest[id][dest] + manifest[dest][id]
            weights += [weight + x for x in path(dest, visited + [id])]
    return weights
        
            



def solution_a():
    maximum_happiness = 0
    for id in manifest.keys():
        maximum_happiness = max(maximum_happiness, *path(id, []))
    return maximum_happiness

def solution_b():
    manifest["Ryan"] = dict()
    for id in manifest.keys():
        if id != "Ryan":
            manifest[id]["Ryan"] = 0
            manifest["Ryan"][id] = 0
    return solution_a()

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

