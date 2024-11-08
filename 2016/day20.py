import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data, limit = examples[0].input_data, 9
data, limit = input_data, 4294967295

data = [(int(line.split("-")[0]), int(line.split("-")[1])) for line in data.split("\n")]
data.sort(key=lambda x: x[0])

def solution_a():
    ip = 0
    for minimum, maximum in data:
        if minimum <= ip <= maximum:
            ip = maximum + 1
        elif ip < minimum:
            break
    return ip

def overlap(start1, end1, start2, end2):
    #from https://nedbatchelder.com/blog/201310/range_overlap_in_two_compares.html
    """Does the range (start1, end1) overlap with (start2, end2)?"""
    return end1 >= start2 and end2 >= start1

def solution_b():
    blacklist = []
    for min1, max1 in data:
        overlap_found = False
        for i in range(len(blacklist)):
            min2, max2 = blacklist[i]
            if overlap(min1, max1, min2, max2):
                blacklist[i] = (min(min1, min2), max(max1, max2))
                overlap_found = True
        if not overlap_found:
            blacklist.append((min1, max1))

    blacklist.sort(key=lambda x: x[0])
    valid_ips = blacklist[0][0]
    for i in range(len(blacklist) - 1):
        valid_ips += blacklist[i + 1][0] - blacklist[i][1] - 1
    valid_ips += limit - blacklist[-1][1]
    return valid_ips
            

    


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

