import sys
from hashlib import md5
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data



def solution_a():
    num = 0
    hex = ""
    while len(hex) < 5 or hex[:5] != "00000":
        num += 1
        hex = md5(f"{data}{num}".encode("utf-8")).hexdigest()
    return num
    

def solution_b(): #takes some time
    num = 0
    hex = ""
    while len(hex) < 6 or hex[:6] != "000000":
        num += 1
        hex = md5(f"{data}{num}".encode("utf-8")).hexdigest()
    return num

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

