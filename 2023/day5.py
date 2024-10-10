from aocd.models import Puzzle
from aocd import examples
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f8bff693a28ddc555a8233386bd6b1ad7e554d5c83830f2ea1712910385002a2567dd54ec3ae2321a7cb563c5dda138661eb4b1697bc4f472" # handout: exclude


def parse_input(data):
    data = [[int(z) for z in list(filter(None, y.split()))] for y in [x.split(":")[1] for x in data.split("\n\n")]]
    return data[1:], data[0]

def overlap(s1, l1, s2, l2):
    """Returns s0, l0, which are the start and length of the overlapping
       section of the ranges defined in the parameters"""
    e1 = s1 + l1 - 1
    e2 = s2 + l2 - 1
    s0 = max(s1, s2)
    l0 = min(e1, e2) - s0 + 1
    return s0, l0

def conv_range(s1, l1, offset):
    return s1 + offset, l1

def find_offset(st, sf): #start to and start from
    return st - sf

def split_range(s, l, ss, sl):
    e = s + l - 1
    se = ss + sl - 1
    
    l1 = ss - s
    l2 = e - se

    return s, l1, ss, sl, se + 1, l2

puzzle = Puzzle(year=2023, day=5)
data = puzzle.examples[0].input_data
#data = puzzle.input_data
data, seeds = parse_input(data)
ranges = seeds.copy()

ans_a = 0
ans_b = 0
for i in range(0, len(data)):
    new_seeds = seeds.copy()
    conv = [0 for i in range(0, len(ranges), 2)]
    for j in range(0, len(data[i]), 3):
        for s, seed in enumerate(seeds):
            if seed in range(data[i][j+1], data[i][j+1] + data[i][j+2]):
                new_seeds[s] += data[i][j] - data[i][j+1]
        """for s in range(0, len(ranges), 2):
            convd = conv.pop(0)
            s1, l1 = ranges.pop(0), ranges.pop(0)
            s2, l2 = data[i][j+1], data[i][j+2]
            s0, l0 = overlap(s1, l1, s2, l2)
            offset = find_offset(data[i][j], data[i][j+1])
            if l0 > 0 and not conv:
                #start prefix, start suffix
                sp, lp, s0, l0, ss, ls = split_range(s1, l1, s0, l0)
                ranges.append(s0 + offset)
                ranges.append(l0)
                conv.append(1)
                if lp > 0:
                    ranges.append(sp)
                    ranges.append(lp)
                    conv.append(0)
                if ls > 0:
                    ranges.append(ss)
                    ranges.append(ls)
                    conv.append(0)
            else:
                ranges.append(s1)
                ranges.append(l1)
                conv.append(0)"""
    seeds = new_seeds

for i in range(0, len(data)):
    conv = [0 for i in range(0, len(ranges))]
    for s in range(0, len(ranges), 2):
        for j in range(0, len(data[i]), 3):
            convd = conv.pop(0)
            s1, l1 = ranges.pop(0), ranges.pop(0)
            s2, l2 = data[i][j+1], data[i][j+2]
            s0, l0 = overlap(s1, l1, s2, l2)
            offset = find_offset(data[i][j], data[i][j+1])
            if l0 > 0 and not conv:
                #start prefix, start suffix
                sp, lp, s0, l0, ss, ls = split_range(s1, l1, s0, l0)
                ranges.append(s0 + offset)
                ranges.append(l0)
                conv.append(1)
                if lp > 0:
                    ranges.append(sp)
                    ranges.append(lp)
                    conv.append(0)
                if ls > 0:
                    ranges.append(ss)
                    ranges.append(ls)
                    conv.append(0)
            else:
                ranges.append(s1)
                ranges.append(l1)
                conv.append(0)
        
ans_a = min(seeds)
seeds = list(ranges[i] for i in range(0, len(ranges), 2))
ans_b = min(seeds)

print(f"Answer 1: {ans_a}")
print(f"Answer 2: {ans_b}")


#puzzle.answer_a = ans_a
#puzzle.answer_b = ans_b