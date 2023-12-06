from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f8bff693a28ddc555a8233386bd6b1ad7e554d5c83830f2ea1712910385002a2567dd54ec3ae2321a7cb563c5dda138661eb4b1697bc4f472" # handout: exclude


def parse_input(data):
    data = data.split("\n")
    return [int(x) for x in list(filter(None, data[0].split(":")[1].split(" ")))], \
        [int(x) for x in list(filter(None, data[1].split(":")[1].split(" ")))]

puzzle = Puzzle(year=2023, day=6)
###data = puzzle.example_data
data = "Time:      7  15   30\nDistance:  9  40  200"
data = puzzle.input_data
times, distances = parse_input(data)
print(times, distances)

ans_a = 1
ans_b = 1
for time, distance in zip(times, distances):
    hold = time // 2 + 1
    go = time - hold
    a = (time + 1) % 2
    while distance < go * hold:
        hold += 1
        go -= 1
        a += 2
    ans_a *= a

time, distance = int("".join([str(x) for x in times])), int("".join([str(x) for x in distances]))
print(time, distance)

hold = time // 2 + 1
go = time - hold
b = (time + 1) % 2
while distance < go * hold:
    hold += 1
    go -= 1
    b += 2
ans_b = b

print(f"Answer 1: {ans_a}")
print(f"Answer 2: {ans_b}")


#puzzle.answer_a = ans_a
puzzle.answer_b = ans_b