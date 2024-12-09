import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
#data = "12345"
data = input_data

disk = [int(x) for x in data]

def solution_a():
    checksum = 0
    blocks = 0
    front = 0
    back = len(disk) - 1
    while front <= back:
        if front % 2 == 0:
            for _ in range(disk[front]):
                checksum += (front // 2) * blocks
                blocks += 1
        else:
            for _ in range(disk[front]):
                checksum += (back // 2) * blocks
                blocks += 1
                disk[back] -= 1
                if disk[back] == 0:
                    back -= 2
                    if front > back:
                        break
        front += 1
    return checksum

def solution_b():
    checksum = 0
    front = 0
    back = len(disk) - 1
    added = [0 for _ in range(len(disk))]
    #back to front scheme
    while 2 <= back:
        front = 1
        while front < back and not (front % 2 == 1 and disk[front] >= disk[back]):
            front += 1
        blocks = sum(disk[:front]) + sum(added[:front])
        for _ in range(disk[back]):
            checksum += (back // 2) * blocks
            blocks += 1
        added[front - 1] += disk[back]
        disk[front] -= disk[back]
        back -= 2
    return checksum

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

