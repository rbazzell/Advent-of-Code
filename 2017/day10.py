import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data, hash_size = examples[0].input_data, 5
data, hash_size = input_data, 256

def knot_hash(l: list[int], lengths, current_position, skip_size):
    for length in lengths:
        indices = [(current_position + i)%len(l) for i in range(length)]
        values = [l[i] for i in indices]
        for i, x in zip(indices, values[::-1]):
            l[i] = x

        current_position = (current_position + length + skip_size) % len(l)
        skip_size += 1
        #print(l, f"skip: {skip_size}   curr: {current_position}")
    return l, current_position, skip_size

def solution_a():
    lengths = [int(x) for x in data.split(",")]
    l = [i for i in range(hash_size)]
    l, _, _ = knot_hash(l, lengths, 0, 0)
    return l[0] * l[1]

def xor(list: list):
    id = list[0]
    for i in range(1, len(list)):
        id ^= list[i]
    return id

def conv_to_hex(num: int):
    return hex(num // 16)[-1] + hex(num % 16)[-1]

def solution_b():
    lengths = [ord(x) for x in data] + [17, 31, 73, 47, 23]
    l = [i for i in range(hash_size)]
    c = s = 0
    for _ in range(64):
        l, c, s = knot_hash(l, lengths, c, s)
    dense = [xor(l[i:i+16]) for i in range(0, len(l), 16)]
    return "".join([conv_to_hex(x) for x in dense])
    


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

