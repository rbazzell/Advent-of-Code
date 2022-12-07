from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=6)
data = puzzle.example_data
data = puzzle.input_data
        
def check_repeats(string):
    for character in string:
        if string.count(character) > 1:
            return True
    return False

start_of_packet = -1
start_of_message = -1
sop = "0000"
som = "00000000000000"

for i in range(len(data)):
    sop = sop[1:] + data[i]
    som = som[1:] + data[i]
    if not check_repeats(sop) and "0" not in sop and start_of_packet < 0:
        start_of_packet = i + 1
    if not check_repeats(som) and "0" not in som and start_of_message < 0:
        start_of_message = i + 1

print(f"a: {start_of_packet}")
#puzzle.answer_a = start_of_packet

print(f"b: {start_of_message}")
puzzle.answer_b = start_of_message