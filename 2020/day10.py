import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[1].input_data
data = input_data

data = data.split("\n")
adapters = [int(x) for x in data]
adapters.append(0)
adapters.sort()
device = adapters[-1] + 3
adapters.append(device)


def solution_a():
    jolts = [0, 0, 0]
    for i in range(1, len(adapters)):
        jolts[adapters[i] - adapters[i - 1] - 1] += 1
    return jolts[0] * jolts[2]

def solution_b():
    paths = [0 for item in adapters]
    explore(paths, 0)
    total = 1
    for path in paths:
        if path == 0:
            return -1
    return paths[0]

    """
    paths = 1
    for i in range(len(adapters)):
        j = i + 1
        while j < len(adapters) and adapters[j] <= adapters[i] + 3:
            paths += 1 
            j += 1
        paths -= 1
    return paths
    """

#maybe a recursive\dynamic algorithm that traces forward? once we know 8 options after picking 17, anything that includes 17 gets multiplied by 8?
    
def explore(paths,i):
    if paths[i] > 0:
        return
    if adapters[i] >= device:
        paths[i] = 1
        return
    total = 0
    j = i + 1
    while j < len(adapters) and adapters[j] <= adapters[i] + 3:
        explore(paths,j)
        total += paths[j]
        j += 1
    paths[i] = total
    return 


#recursive solution - works for examples, but not for actual set (takes ~2 hours to run)
def explore_old(i):
    if adapters[i] >= device:
        return 1
    paths = 0
    j = i + 1
    while adapters[j] <= adapters[i] + 3:
        paths += explore_old(j)
        j += 1
    return paths

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

