import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
#data = "1000\n17,x,13,19"
data = input_data

data = data.split("\n")

time = int(data[0])
buses = [int(x) for x in data[1].replace("x,", "").split(",")]

def solution_a():
    curr_time = time - 1
    early_bus = 0
    while not early_bus:
        curr_time += 1
        for bus in buses:
            if curr_time % bus == 0:
                early_bus = bus
                break
    return early_bus * (curr_time - time)

def solution_b():
    goal = list()
    i = 0
    for item in data[1].split(","):
        if item != 'x':
            goal.append(i)
        i += 1
    
    time = 0
    digit_value = buses[0]
    for i in range(1, len(buses)):
        time += find_increment(digit_value, time + goal[i], buses[i]) * digit_value
        digit_value *= buses[i]
    return time

def find_increment(digit_value, offset, base): #offset is goal plus previously calculated number
    for x in range(1, base):
        if (digit_value * x + offset) % base == 0:
            return x
    return 0

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

