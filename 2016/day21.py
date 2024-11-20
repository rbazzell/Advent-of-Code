import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data, start, scramble = examples[0].input_data, "abcde", "decab"
data, start, scramble = input_data, "abcdefgh", "fbgdceah"

data = data.split("\n")
instructions = []
for line in data:
    line = line.split(" ")
    command = line[0]
    match command:
        case "swap":
            type = line[1]
            if type == "position":
                x = int(line[2])
                y = int(line[-1])
            else: # type == "letter"
                x = line[2]
                y = line[-1]
            payload = (type, x, y)
        case "rotate":
            type = line[1]
            if type == "left" or type == "right":
                x = int(line[2])
            else: # type == "based"
                x = line[-1]
            payload = (type, x)
        case "reverse" | "move":
            x = int(line[2])
            y = int(line[-1])
            payload = (x, y)
    instructions.append((command, payload))
    

def solution_a(string: str = start):
    for command, payload in instructions:
        match command:
            case "swap":
                type, x, y = payload
                if type == "letter":
                    x, y = string.find(x), string.find(y)
                temp = string[x]
                string = string[:x] + string[y] + string[x+1:]
                string = string[:y] + temp + string[y+1:]
            case "rotate":
                type, x = payload
                if type == "based":
                    x = string.find(x)
                    x += 2 if x >= 4 else 1
                    x %= len(string)
                if type == "left":
                    string = string[x:] + string[:x]
                else: #type == "right":
                    string = string[-x:] + string[:-x]
            case "reverse":
                x, y = payload
                string = string[:x] + string[x:y+1][::-1] + string[y+1:] 
            case "move":
                x, y = payload
                temp = string[x]
                string = string[:x] + string[x+1:]
                string = string[:y] + temp + string[y:]
    return string

def solution_b(string: str = scramble):
    for command, payload in instructions[::-1]:
        match command:
            case "swap":
                type, x, y = payload
                if type == "letter":
                    x, y = string.find(x), string.find(y)
                temp = string[x]
                string = string[:x] + string[y] + string[x+1:]
                string = string[:y] + temp + string[y+1:]
            case "rotate":
                type, x = payload
                if type == "based":
                    x = string.find(x)
                    x = 8 if x == 0 else x
                    x = (x+1)//2 if x % 2 == 1 else (x//2) + 5
                    x %= len(string)
                if type == "left":
                    string = string[-x:] + string[:-x]
                else: #type == "right":
                    string = string[x:] + string[:x]
            case "reverse":
                x, y = payload
                string = string[:x] + string[x:y+1][::-1] + string[y+1:] 
            case "move":
                x, y = payload
                temp = string[y]
                string = string[:y] + string[y+1:]
                string = string[:x] + temp + string[x:]
    return string
    
print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

