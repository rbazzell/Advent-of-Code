from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f8bff693a28ddc555a8233386bd6b1ad7e554d5c83830f2ea1712910385002a2567dd54ec3ae2321a7cb563c5dda138661eb4b1697bc4f472" # handout: exclude


def parse_input(data):
    data = [[int(z) for z in list(filter(None, y.split()))] for y in [x.split(":")[1] for x in data.split("\n\n")]]
    return data[1:], data[0]

def split_range(s1, l1, s2, l2):
    split = find_split(s1, l1, s2, l2)
    if split < 0:
        pass



def find_split(s1, l1, s2, l2):
    e1 = s1 + l1
    e2 = s2 + l2
    if s1 == s2 and l1 == l2:
        return s1
    if s1 < s2 and e1 >= s2:
        return
    


puzzle = Puzzle(year=2023, day=5)
data = puzzle.example_data
data = puzzle.input_data
data, seeds = parse_input(data)
ranges = seeds.copy()

ans_a = 0
ans_b = 0
for i in range(0, len(data)):
    new_seeds = seeds.copy()
    for j in range(0, len(data[i]), 3):
        for s, seed in enumerate(seeds):
            if seed in range(data[i][j+1], data[i][j+1] + data[i][j+2]):
                new_seeds[s] += data[i][j] - data[i][j+1]
        for s in range(0, len(ranges), 2):
            ranges[s] = 0
            pass
    seeds = new_seeds
ans_a = min(seeds)

print(shift_range(range(5), 5))


print(f"Answer 1: {ans_a}")
print(f"Answer 2: {ans_b}")


#puzzle.answer_a = ans_a
#puzzle.answer_b = ans_b