import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

class Display():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [['.' for w in range(width)] for h in range(height)]

    def rect(self, a: int, b: int):
        for x in range(a):
            for y in range(b):
                self.grid[y][x] = "#"
    
    def rotate(self, type: str, a: int, b: int):
        if type == "row":
            self.rotate_row(a, b)
        elif type == "column":
            self.rotate_col(a, b)
        
    def rotate_row(self, a: int, b: int):
        self.grid[a] = self.grid[a][-b:] + self.grid[a][:-b]

    def rotate_col(self, a: int, b: int):
        col = []
        for y in range(len(self.grid)):
            col.append(self.grid[y][a])

        col = col[-b:] + col[:-b]

        for y in range(len(self.grid)):
            self.grid[y][a] = col[y]

    def count_on(self):
        on = 0
        for row in self.grid:
            for c in row:
                if c == "#":
                    on += 1
        return on
    
    def __repr__(self):
        return aocu.grid_str(self.grid)

    def clear(self):
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] == ".":
                    self.grid[r][c] = " "


instructions = []
for line in data:
    line = line.split(" ")
    command = line[0]
    instruction = [command]
    match command:
        case "rect":
           line = line[1].split("x")
           a = int(line[0])
           b = int(line[1])
           instruction.append(a)
           instruction.append(b)
        case "rotate":
            type = line[1]
            a = int(line[2][2:])
            b = int(line[-1])
            instruction.append(type)
            instruction.append(a)
            instruction.append(b)
    instructions.append(instruction)

def solution_a():
    display = Display(50, 6)
    for instruction in instructions:
        match instruction[0]:
            case "rect":
                display.rect(instruction[1], instruction[2])
            case "rotate":
                display.rotate(instruction[1], instruction[2], instruction[3])
    return display.count_on()
    

def solution_b():
    display = Display(50, 6)
    for instruction in instructions:
        match instruction[0]:
            case "rect":
                display.rect(instruction[1], instruction[2])
            case "rotate":
                display.rotate(instruction[1], instruction[2], instruction[3])
    display.clear()
    return display


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

