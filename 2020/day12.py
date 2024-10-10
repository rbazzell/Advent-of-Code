import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
from enum import Enum

puzzle = aocu.get_puzzle(12, 2020)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")
directions = [(x[0], int(x[1:])) for x in data]

def solution_a():
    facing = 90 # 0 is N, 90 is E, 180 is S, 270 is W
    ns_pos = 0
    ew_pos = 0
    for command, value in directions:
        match command[0]:
            case "N":
                ns_pos += value
            case "S":
                ns_pos -= value
            case "E":
                ew_pos += value
            case "W":
                ew_pos -= value
            case "L":
                facing -= value
                facing %= 360
            case "R":
                facing += value
                facing %= 360
            case "F":
                match facing:
                    case 0:
                        ns_pos += value
                    case 90:
                        ew_pos += value
                    case 180:
                        ns_pos -= value
                    case 270:
                        ew_pos -= value
    return abs(ns_pos) + abs(ew_pos)

def solution_b():
    ship = [0, 0]
    waypoint = [10, 1]
    for command, value in directions:
        match command[0]:
            case "N":
                waypoint[1] += value
            case "S":
                waypoint[1] -= value
            case "E":
                waypoint[0] += value
            case "W":
                waypoint[0] -= value
            case "L":
                for i in range(value//90):
                    waypoint = rotate(waypoint, True)
            case "R":
                for i in range(value//90):
                    waypoint = rotate(waypoint, False)
            case "F":
                ship[0] += waypoint[0] * value
                ship[1] += waypoint[1] * value
    return abs(ship[0]) + abs(ship[1])

def rotate(p, ccw=True): #only rotates 90 degrees
    if ccw:
        return [-p[1], p[0]]
    else:
        return [p[1], -p[0]]

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

