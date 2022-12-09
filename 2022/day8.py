from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=8)
data = puzzle.example_data
data = puzzle.input_data

def check_up(row, tree, data):
    for i in range(row - 1, -1, -1):
        if not data[i][tree] < data[row][tree]:
            return False
    return True

def check_down(row, tree, data):
    for i in range(row + 1, len(data)):
        if not data[i][tree] < data[row][tree]:
            return False
    return True

def check_right(row, tree, data):
    for i in range(tree + 1, len(data[0])):
        if not data[row][i] < data[row][tree]:
            return False
    return True

def check_left(row, tree, data):
    for i in range(tree - 1, -1, -1):
        if not data[row][i] < data[row][tree]:
            return False
    return True

def check_all(row, tree, data):
    return check_up(row, tree, data) or check_down(row, tree, data) or check_left(row, tree, data) or check_right(row, tree, data)


def scenic_up(row, tree, data):
    score = 0
    for i in range(row - 1, -1, -1):
        if data[i][tree] < data[row][tree]:
            score += 1
        if data[i][tree] >= data[row][tree]:
            return score + 1
    return score

def scenic_down(row, tree, data):
    score = 0
    for i in range(row + 1, len(data)):
        if data[i][tree] < data[row][tree]:
            score += 1
        if data[i][tree] >= data[row][tree]:
            return score + 1
    return score

def scenic_right(row, tree, data):
    score = 0
    for i in range(tree + 1, len(data[0])):
        if data[row][i] < data[row][tree]:
            score += 1
        if data[row][i] >= data[row][tree]:
            return score + 1
    return score

def scenic_left(row, tree, data):
    score = 0
    for i in range(tree - 1, -1, -1):
        if data[row][i] < data[row][tree]:
            score += 1
        if data[row][i] >= data[row][tree]:
            return score + 1
    return score

def scenic_score(row, tree, data):
    return scenic_up(row, tree, data) * scenic_down(row, tree, data) * scenic_left(row, tree, data) * scenic_right(row, tree, data)


data = [[int(y) for y in x] for x in data.split("\n")]

visible_trees = 2 * len(data) + 2 * len(data[0]) - 4

most_scenic_score = 0
for row in range(1, len(data) - 1):
    for tree in range(1, len(data[0]) - 1):
        #print(f"({row}, {tree}, {data[row][tree]}) ==> {scenic_score(row, tree, data)}")
        if check_all(row, tree, data):
            visible_trees += 1
        if scenic_score(row, tree, data) > most_scenic_score:
            most_scenic_score = scenic_score(row, tree, data)


print(f"a: {visible_trees}")
#puzzle.answer_a = visible_trees

print(f"b: {most_scenic_score}")
puzzle.answer_b = most_scenic_score