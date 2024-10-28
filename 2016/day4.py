import sys, heapq
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

def count_letters(s:str):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    counts = dict()
    for letter in ALPHABET:
        counts[letter] = s.count(letter)
    return counts

def sumcheck(checksum:str, counts:dict[str:int]):
    counts = sorted(counts, key=counts.get, reverse=True)
    return checksum == "".join(counts[:5])

def rotate(s:str, n:int):
    new_s = ""
    for c in s:
        if c == "-":
            new_s += " "
        else:
            new_s += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    return new_s


def solution_a():
    total = 0
    for line in data:
        checksum = line[-6:-1]
        id = int(line[-10:-7])
        letter_count = count_letters(line[:-10])
        if sumcheck(checksum, letter_count):
            total += id
    return total



def solution_b():
    for line in data:
        checksum = line[-6:-1]
        id = int(line[-10:-7])
        letter_count = count_letters(line[:-10])
        if sumcheck(checksum, letter_count):
            line = rotate(line[:-10], id)
            if "northpole" in line:
                return id
    return -1

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

