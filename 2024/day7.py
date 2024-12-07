import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
from time import time

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

calibrations = {int(line.split(": ")[0]): tuple(int(x) for x in line.split(": ")[1].split())[::-1] for line in data.split("\n")}

#about 10x faster than brute force on full input
def solution_a():
    total = 0
    for result, nums in calibrations.items():
        queue = {result}
        for num in nums[:-1]:
            new_queue = set()
            while queue:
                curr_op_result = queue.pop()
                if curr_op_result % num == 0:
                    new_queue.add(curr_op_result // num)
                new_queue.add(curr_op_result - num)
            queue = new_queue
        if nums[-1] in queue:
            total += result
    return total

def solution_a_brute():
    total = 0
    for result, nums in calibrations.items():
        nums = nums[::-1]
        queue = {nums[0]}
        for num in nums[1:]:
            new_queue = set()
            while queue:
                curr_op_result = queue.pop()
                new_queue.add(curr_op_result * num)
                new_queue.add(curr_op_result + num)
            queue = new_queue
        if result in queue:            
            total += result
    return total

def solution_b():
    total = 0
    for result, nums in calibrations.items():
        nums = nums[::-1]
        queue = {nums[0]}
        for num in nums[1:]:
            new_queue = set()
            while queue:
                curr_op_result = queue.pop()
                new_queue.add(curr_op_result * num)
                new_queue.add(curr_op_result + num)
                new_queue.add(concat(curr_op_result, num))
            queue = new_queue
        if result in queue:            
            total += result
    return total

def concat (a: int, b:int):
    return int(str(a)+str(b))

start = time()
solution_a()
print(f"Optimized: {time() - start}")
start = time()
solution_a_brute()
print(f"Brute Force: {time() - start}")


print(solution_a())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

