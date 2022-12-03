from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=2)
#data = puzzle.example_data
data = puzzle.input_data

data = [[ord(y) - 64 for y in x.split(" ")] for x in data.split("\n")]
for line in data:
    line[1] -= 23

#data = [[1, 1], [1, 2], [1, 3], 
#        [2, 1], [2, 2], [2, 3],
#        [3, 1], [3, 2], [3, 3]]

score_a = 0
score_b = 0
for line in data:
    if line[1] == line[0]:
        score_a += 3 + line[1] # draw case
    elif line[1] - line[0] == 1 or (line[0] == 3 and line[1] == 1):
        score_a += 6 + line[1] # win case
    else:
        score_a += 0 + line[1] # loss case

    match line[1]:
        case 1: # loss case
            score_b += 0 + line[0] - 1
            if line[0] == 1:
                score_b += 3
        case 2: # draw case
            score_b += 3 + line[0]
        case 3: # win case
            score_b += 6 + line[0] + 1
            if line[0] == 3:
                score_b -= 3
        case _:
            pass


print(f"a: {score_a}")
#puzzle.answer_a = score_a

print(f"b: {score_b}")
puzzle.answer_b = score_b