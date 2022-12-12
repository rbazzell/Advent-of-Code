from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

def isadjacent(a, b):
    return a[0] - 1 <= b[0] <= a[0] + 1 and a[1] - 1 <= b[1] <= a[1] + 1

def isleft(a, b):
    return a[0] <= b[0]

def isright(a, b):
    return a[0] >= b[0]

def isdown(a, b):
    return a[1] <= b[1]

def isup(a, b):
    return a[1] >= b[1]

def follow(a, b):
    match (isleft(a, b), isright(a, b), isdown(a, b), isup(a, b)):
        case (True, False, True, True): #a is left of b, move b left 1
            b[0] -= 1
        case (False, True, True, True): #a is right of b, move b right 1
            b[0] += 1
        case (True, True, True, False): #a is below b, move b down 1
            b[1] -=1
        case (True, True, False, True): #a is above b, move b up 1
            b[1] += 1
        case (True, False, False, True): #a is UL b, move b left and up 1
            b[0] -= 1
            b[1] += 1
        case (True, False, True, False): #a is DL b, move b left and down 1
            b[0] -= 1
            b[1] -= 1
        case (False, True, False, True): #a is UR b, move b up and right 1
            b[0] += 1
            b[1] += 1
        case(False, True, True, False): #a is DR b, move b down and right 1
            b[0] += 1
            b[1] -= 1

puzzle = Puzzle(year=2022, day=9)

with open('2022\\examples\\day9example2.txt', 'r') as f:
    data = f.read()
data = puzzle.input_data
data = [[line.split(" ")[0], int(line.split(" ")[1])] for line in data.split("\n")]

visited_a = []
visited_b = []
rope_a = [[0, 0] for i in range(2)]
rope_b = [[0, 0] for i in range(10)]

def move(rope, data, visited):
    for direction, distance in data:
        for i in range(distance):
            match direction:
                case 'L':
                    rope[0][0] -= 1
                case 'R':
                    rope[0][0] += 1
                case 'D':
                    rope[0][1] -= 1
                case 'U':
                    rope[0][1] += 1
            for i in range(1, len(rope)):
                if not isadjacent(rope[i - 1], rope[i]):
                    follow(rope[i - 1], rope[i])
            if rope[-1] not in visited:
                visited.append(rope[-1].copy())

move(rope_a, data, visited_a)
move(rope_b, data, visited_b)

print(f"a: {len(visited_a)}")
puzzle.answer_a = len(visited_a)

print(f"b: {len(visited_b)}")
puzzle.answer_b = len(visited_b)