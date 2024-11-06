import sys
from hashlib import md5
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

salt = data

def solution_a():
    triples = tuple(f"{x}{x}{x}" for x in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
    quintuples = tuple(f"{x}{x}{x}{x}{x}" for x in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
    i = 0
    keys = []
    checking: dict[str, list[int]] = {}
    for chs in triples:
        checking[chs[0]] = list()
    while len(keys) < 64:
        hash = md5(f"{salt}{i}".encode()).hexdigest()
        possibly_a_key = False
        for j in range(len(hash) - 2):
            if j+5 <= len(hash) and hash[j:j+5] in quintuples:
                for index in checking[hash[j]]:
                    if index + 1000 >= i:
                        keys.append(index)
                checking[hash[j]].clear()
            if not possibly_a_key and hash[j:j+3] in triples:
                checking[hash[j]].append(i)
                possibly_a_key = True
        i += 1
    return keys[63]





def solution_b():
    triples = tuple(f"{x}{x}{x}" for x in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
    quintuples = tuple(f"{x}{x}{x}{x}{x}" for x in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
    i = 0
    keys = []
    checking: dict[str, list[int]] = {ch: [] for ch in "0123456789abcdef"}
    while len(keys) < 64:
        hash = md5(f"{salt}{i}".encode()).hexdigest()
        for stretch in range(2016):
            hash = md5(hash.encode()).hexdigest()
        for j in range(len(hash) - 4):
            if hash[j:j+5] in quintuples:
                for index in checking[hash[j]]:
                    if index + 1000 >= i:
                        keys.append(index)
                checking[hash[j]].clear()
        for j in range(len(hash) - 2):
            if hash[j:j+3] in triples:
                checking[hash[j]].append(i)
                break
        i += 1
    return keys[63]


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

