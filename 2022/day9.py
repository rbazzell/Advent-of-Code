from aocd.models import Puzzle
from copy import deepcopy
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=9)

with open('2022\\examples\\day9example.txt', 'r') as f:
    data = f.read()
#data = puzzle.input_data
data = [[line.split(" ")[0], int(line.split(" ")[1])] for line in data.split("\n")]


def isadjacent_a(a, b):
    return a[0] - 1 <= b[0] <= a[0] + 1 and a[1] - 1 <= b[1] <= a[1] + 1


def isadjacent_b(a, b):
    return a['x'] - 1 <= b['x'] <= a['x'] + 1 and a['y'] - 1 <= b['y'] <= a['y'] + 1
    return a[0] - 1 <= b[0] <= a[0] + 1 and a[1] - 1 <= b[1] <= a[1] + 1


def solve_a():
    head = [0, 0] # marked as [x, y], x is horizontal, y is vertical
    tail = [0, 0]

    tail_visited = [tail.copy()] # add as (x, y, v), where v is the number of times this square was visited

    for direction, distance in data:
        for i in range(distance):
            prev_head = head.copy()
            match direction:
                case 'U':
                    head[1] += 1
                case 'D':
                    head[1] -= 1
                case 'R':
                    head[0] += 1
                case 'L':
                    head[0] -= 1
            if not isadjacent_a(head, tail):
                tail = prev_head.copy()
                if tail not in tail_visited:
                    tail_visited.append(tail.copy())
    return len(tail_visited)
        

def solve_b():
    tail_visited = [[0, 0]]
    rope = [{'x':0, 'y':0} for i in range(10)]
    for direction, distance in data:
        for i in range(distance):
            prev_rope = deepcopy(rope)
            match direction:
                case 'U':
                    rope[0]['y'] += 1
                case 'D':
                    rope[0]['y'] -= 1
                case 'R':
                    rope[0]['x'] += 1
                case 'L':
                    rope[0]['x'] -= 1
            if not isadjacent_b(rope[0], rope[1]):
                rope[1] = prev_rope[0].copy()
                if rope[1] not in tail_visited:
                    tail_visited.append(rope[1].copy())
    return len(tail_visited)

        
        




print(f"a: {solve_a()}")
#puzzle.answer_a = solve_a()

print(f"b: {solve_b()}")
#puzzle.answer_b = most_scenic_score