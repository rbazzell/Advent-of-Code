import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data, disk_size = examples[1].input_data, 20
data, disk_size = input_data, 272

initial_state = data

#NOTE: FIND MATHY WAY TO DO THIS WITH INTEGERS
def start_dragon(bits: str) -> str:
    a = bits
    b = "".join("0" if x == "1" else "1" for x in bits[::-1])
    return f"{a}0{b}"
    


def checksum(bits: str, segment_length: int) -> str:
    checksum = ""
    for i in range(0, len(bits), segment_length):
        if bits[i:i+segment_length].count("1") % 2:
            checksum += "0"
        else:
            checksum += "1"
    return checksum
            

def solution_a():
    disk_size = 272
    disk_data : str = start_dragon(initial_state)
    while len(disk_data) < disk_size:
        middle = len(disk_data) // 2
        disk_data = disk_data + "0" + disk_data[:middle] + "1" + disk_data[middle+1:]
    disk_data = disk_data[:disk_size]

    segment_length = disk_size
    while segment_length % 2 != 1:
        segment_length //= 2
    segment_length = disk_size // segment_length
        
    return checksum(disk_data, segment_length)


def solution_b():
    disk_size = 35651584
    disk_data : str = start_dragon(initial_state)
    while len(disk_data) < disk_size:
        middle = len(disk_data) // 2
        disk_data = disk_data + "0" + disk_data[:middle] + "1" + disk_data[middle+1:]
    disk_data = disk_data[:disk_size]

    segment_length = disk_size
    while segment_length % 2 != 1:
        segment_length //= 2
    segment_length = disk_size // segment_length
        
    return checksum(disk_data, segment_length)


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

