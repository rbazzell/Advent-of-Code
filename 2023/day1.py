from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f8bff693a28ddc555a8233386bd6b1ad7e554d5c83830f2ea1712910385002a2567dd54ec3ae2321a7cb563c5dda138661eb4b1697bc4f472" # handout: exclude

puzzle = Puzzle(year=2023, day=1)
#data = puzzle.example_data
data = puzzle.input_data
#data = """two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"""

data = data.split("\n")

def find_first_int(line : str):
    for char in line:
        if char.isdigit():
            return char
        
def find_first_num(line : str, reverse=False):
    for i, c in enumerate(line):
        if c.isdigit():
            return c
        elif line[i:i+3] == ("one" if not reverse else "eno"):
            return '1'
        elif line[i:i+3] == ("two" if not reverse else "owt"):
            return '2'
        elif line[i:i+5] == ("three" if not reverse else "eerht"):
            return '3'
        elif line[i:i+4] == ("four" if not reverse else "ruof"):
            return '4'
        elif line[i:i+4] == ("five" if not reverse else "evif"):
            return '5'
        elif line[i:i+3] == ("six" if not reverse else "xis"):
            return '6'
        elif line[i:i+5] == ("seven" if not reverse else "neves"):
            return '7'
        elif line[i:i+5] == ("eight" if not reverse else "thgie"):
            return '8'
        elif line[i:i+4] == ("nine" if not reverse else "enin"):
            return '9'

        

sum_a = 0
sum_b = 0
for line in data:
    sum_a += int(find_first_int(line) + find_first_int(line[::-1]))
    sum_b += int(find_first_num(line) + find_first_num(line[::-1], True))

#puzzle.answer_a = sum_a
puzzle.answer_b = sum_b

