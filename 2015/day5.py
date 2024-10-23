import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[5].input_data
data = input_data

data = data.split("\n")

def solution_a():
    nice = 0
    for string in data:
        vowels = sum([string.count(x) for x in ('a','e','i','o','u')])
        double_letters = sum([string.count(x) for x in ('aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz')])
        disqualified = sum([string.count(x) for x in ('ab','cd','pq','xy')])
        if not disqualified and vowels >= 3 and double_letters:
            nice += 1
    return nice

def solution_b():
    nice = 0
    a_z = tuple(chr(x) for x in range(ord('a'), ord('z') + 1))
    a_z_2 = tuple(f"{x}{y}" for x in a_z for y in a_z) #every pair of {a-z}{a-z}
    a_z_3 = tuple(f"{x}{y}{x}" for x in a_z for y in a_z) #every substring of X{a-z}X such that X={a-z}
    for string in data:
        pairs = sum([string.count(x) for x in a_z_2 if string.count(x) >= 2])
        repeats = sum([string.count(x) for x in a_z_3])
        if pairs and repeats:
            nice += 1
    return nice

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

