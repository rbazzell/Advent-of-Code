from aocd.models import Puzzle
import os, sys
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=7)

with open('2022\\examples\\day7example.txt', 'r') as f:
    data = f.read()
#data = puzzle.input_data

def find_in_list(array, target, near_index):
    check_array = list()
    for item in array:
        if item[1] == target and item[0] > near_index:
            check_array.append(item)
    closest_item = (sys.maxsize, None, 0)
    for item in check_array:
        if item[0] < closest_item[0]:
            closest_item = item
    return closest_item

data = data.split("\n")

directories = list() # used as a stack
visited = list() # used to preserve the cost of the calculated directories

total_used_space = 0
for i, line in enumerate(data):
    line = line.split(" ")
    if line[0] + line[1] == "$cd" and line[2] != "..": # file size
        directories.append((i, line[2]))
    if line[0].isdigit():
        total_used_space += int(line[0])

for i, directory in reversed(directories):
    size = 0
    j = i + 2
    while j < len(data) and data[j][0] != "$":
        command = data[j].split(" ")
        if command[0].isdigit():
            size += int(command[0])
        elif command[0] == "dir":
            size += find_in_list(visited, command[1], i)[2]
        j += 1
    visited.append((i, directory, size))

visited[-1] = (visited[-1][0], visited[-1][1], total_used_space)
print(visited)
print(total_used_space)
space_to_free = 30000000 - (70000000 - total_used_space)
print(space_to_free)
ans_a = 0
ans_b = sys.maxsize
for directory in visited:
    if directory[2] < 100000:
        ans_a += directory[2]
    if directory[2] > space_to_free and directory[2] < ans_b:
        ans_b = directory[2]
        


print(f"a: {ans_a}")
#puzzle.answer_a = ans_a

print(f"b: {ans_b}")
#puzzle.answer_b = ans_b       