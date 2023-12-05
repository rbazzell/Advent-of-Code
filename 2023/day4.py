from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f8bff693a28ddc555a8233386bd6b1ad7e554d5c83830f2ea1712910385002a2567dd54ec3ae2321a7cb563c5dda138661eb4b1697bc4f472" # handout: exclude


def parse_input(data):
    return [[list(filter(None, y.split(" "))) for y in x.split(":")[1].split("|")] for x in data.split("\n")]

puzzle = Puzzle(year=2023, day=4)
#data = puzzle.example_data
data = puzzle.input_data
print(data)
data = parse_input(data)
copies = [1 for x in range(len(data))]



sum_a = 0
sum_b = 0
for i, card in enumerate(data):
    card_total = 0
    for num in card[1]:
        if num in card[0]:
            card_total += 1
    sum_a += 0 if card_total == 0 else 1 << (card_total - 1)
    for j in range(i + 1, i + 1 + card_total if i + 1 + card_total < len(copies) else len(copies)):
        copies[j] += copies[i]

sum_b = sum(copies)




print(f"Answer 1: {sum_a}")
print(f"Answer 2: {sum_b}")


#puzzle.answer_a = sum_a
puzzle.answer_b = sum_b