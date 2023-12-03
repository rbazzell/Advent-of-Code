from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f8bff693a28ddc555a8233386bd6b1ad7e554d5c83830f2ea1712910385002a2567dd54ec3ae2321a7cb563c5dda138661eb4b1697bc4f472" # handout: exclude

def parse_input(data):
    data = data.split("\n")
    for i, line in enumerate(data):
        data[i] = [[{z.split()[1]:int(z.split()[0]) for z in y.split(',')} for y in x.split(";")] for x in line.split(":")[1:]][0]
    return data

def check_game(game_number, game):
    for round in game:
        for key in round:
            if round[key] > MARBLE_MAX[key]:
                return 0
    return game_number

def deter_max(game):
    maxes = {'red':0,'green':0,'blue':0}
    for round in game:
        for key in round:
            if round[key] > maxes[key]:
                maxes[key] = round[key]
    return maxes['red']*maxes['green']*maxes['blue']



puzzle = Puzzle(year=2023, day=2)
#data = puzzle.example_data
data = puzzle.input_data
MARBLE_MAX = {'red':12,'green':13,'blue':14}
data = parse_input(data)



sum_a = 0
sum_b = 0
for i, game in enumerate(data):
    sum_a += check_game(i + 1, game)
    sum_b += deter_max(game)


        
print(sum_b)
#puzzle.answer_a = sum_a
puzzle.answer_b = sum_b

