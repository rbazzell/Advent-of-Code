from aocd.models import Puzzle
import os
import functools
os.environ["AOC_SESSION"] = "53616c7465645f5f8bff693a28ddc555a8233386bd6b1ad7e554d5c83830f2ea1712910385002a2567dd54ec3ae2321a7cb563c5dda138661eb4b1697bc4f472" # handout: exclude


def parse_input(data):
    data = data.split("\n\n")
    return data[0], {x[0:3] : (x[7:10], x[12:15]) for x in data[1].split("\n")}

def solve_regular(directions, nodes):
    steps = 0 # number of steps from AAA to end
    curr = "AAA"
    i = 0 #to know which direction to follow
    while curr != "ZZZ":
        steps += 1
        curr = nodes[curr][0 if directions[i] == "L" else 1]
        i = steps % len(directions)
    return steps

def all_end_in_z(node_names):
    for name in node_names:
        if name[-1] != "Z":
            return False
    return True


def length_from_A_to_Z(curr):
    steps = 0
    i = 0
    while curr[-1] != "Z":
        steps += 1
        curr = nodes[curr][0 if directions[i] == "L" else 1]
        i = steps % len(directions)
    return steps, curr


def length_from_Z_to_Z(curr, start_z, sofar):
    steps = sofar
    i = steps % len(directions)
    steps += 1
    curr = nodes[curr][0 if directions[i] == "L" else 1]
    while curr[-1] != "Z":
        i = steps % len(directions)
        curr = nodes[curr][0 if directions[i] == "L" else 1]
        steps += 1

    return curr, start_z == curr, steps - sofar


def solve_ghost(directions, nodes):
    steps = 0
    curr = [x for x in nodes.keys() if x[-1] == "A"]
    path = [list() for x in range(len(curr))]
    for n, node in enumerate(curr):
        path[n].append(node)
        cost, node = length_from_A_to_Z(node)
        loop = True
        while loop:
            path[n].append(node)
            steps += cost
            node, loop, cost = length_from_Z_to_Z(path[n][-1], path[n][1], steps)
    return steps
            






    """steps = 0
    curr = [x for x in nodes.keys() if x[-1] == "A"]
    zs = [x for x in nodes.keys() if x[-1] == "Z"]
    print(curr, zs)
    i = 0 #to know which direction to follow
    while not all_end_in_z(curr):
        steps += 1
        curr = [nodes[x][0 if directions[i] == "L" else 1] for x in curr]
        i += 1
        if i >= len(directions):
            i = 0
    return steps"""


puzzle = Puzzle(year=2023, day=8)
#data = puzzle.examples[0].input_data

data = """LR

11A = (11B, XXX)
11B = (XXX, 11C)
11C = (11Z, XXX)
11Z = (11B, 11C)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

#data = puzzle.input_data
directions, nodes = parse_input(data)

#ans_a = solve_regular(directions, nodes)
ans_b = solve_ghost(directions, nodes)



#print(f"Answer 1: {ans_a}")
print(f"Answer 2: {ans_b}")


#puzzle.answer_a = ans_a