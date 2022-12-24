from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

class Sand:
    walls = list()
    def __init__(self, walls):
        Sand.walls = walls
        self.coords = (500, 0)
    
    def get_coords(self):
        return self.coords

    def move(self, sands):
        if self.can_move_down(sands):
            self.coords = (self.coords[0], self.coords[1] + 1)
        elif self.can_move_down_left(sands):
            self.coords = (self.coords[0] - 1, self.coords[1] + 1)
        elif self.can_move_down_right(sands):
            self.coords = (self.coords[0] + 1, self.coords[1] + 1)
        else:
            return False
        return True

    def can_move_down(self, sands):
        new_coords = (self.coords[0], self.coords[1] + 1)
        return new_coords not in Sand.walls

    def can_move_down_left(self, sands):
        new_coords = (self.coords[0] - 1, self.coords[1] + 1)
        return new_coords not in Sand.walls
    
    def can_move_down_right(self, sands):
        new_coords = (self.coords[0] + 1, self.coords[1] + 1)
        return new_coords not in Sand.walls

    def __repr__(self):
        return f"({self.coords[0]}, {self.coords[1]})"

    def compare(self, tup:tuple):
        return self.coords is tup

def print_representation(og_walls, walls):
    # 435 to 560 on x,
    # 0 to 161 on y
    for y in range(160):
        for x in range(435, 560):
            if (x, y) == (500, 0):
                print("+", end="")
            elif (x, y) in og_walls:
                print("#", end="")
            elif (x, y) in walls:
                print("O", end="")
            else:
                print(".", end="")
        print(f"[{y}]")
            


#much simplier solution using a large 2d array, wouldn't get bogged down on so many linear searches

puzzle = Puzzle(year=2022, day=14)
data = puzzle.example_data
data = puzzle.input_data
data = [[(int(point.split(",")[0]), int(point.split(",")[1])) for point in line.split(" -> ")] for line in data.split("\n")]
walls = []
max_y = 0
for line in data:
    for i in range(len(line) - 1):
        if line[i][1] > max_y:
            max_y = line[i][1]
        if line[i][0] == line[i + 1][0] and line[i][1] < line[i + 1][1]:
            for j in range(line[i][1], line[i + 1][1] + 1):
                if (line[i][0], j) not in walls:
                    walls.append((line[i][0], j))
        elif line[i][0] == line[i + 1][0] and line[i][1] > line[i + 1][1]:
            for j in range(line[i][1], line[i + 1][1] - 1, -1):
                if (line[i][0], j) not in walls:
                    walls.append((line[i][0], j))
        elif line[i][1] == line[i + 1][1] and line[i][0] < line[i + 1][0]:
            for j in range(line[i][0], line[i + 1][0] + 1):
                if (j, line[i][1]) not in walls:
                    walls.append((j, line[i][1]))
        else:
            for j in range(line[i][0], line[i + 1][0] - 1, -1):
                if (j, line[i][1]) not in walls:
                    walls.append((j, line[i][1]))
    if line[-1][1] > max_y:
            max_y = line[-1][1]

og_walls = walls.copy()
sands: list[Sand] = list() # list of x, y tuples

while True:
    #print_representation(og_walls, walls)
    #print("\n\n\n\n\n\n\n")
    sands.append(Sand(walls))
    while sands[-1].move(sands):
        if sands[-1].coords[1] == 10000:
            break
    else:
        walls.append(sands[-1].get_coords())
        continue
    break
ans_a = len(sands) - 1

#reset for part b
sands: list[Sand] = list()
walls = og_walls.copy()

#add "infinite" line

for x in range(-250, 750):
    walls.append((x, max_y + 2))
og_walls = walls.copy()

while True:
    if len(sands) % 10000 == 0:
        print_representation(og_walls, walls)
        print("\n\n\n\n\n\n\n")
    sands.append(Sand(walls))
    while sands[-1].move(sands):
        if sands[-1].coords == (500, 0):
            break
    else:
        walls.append(sands[-1].get_coords())
        if sands[-1].coords == (500, 0):
            break
        continue
ans_b = len(sands)
    




print(f"a: {ans_a}")
#puzzle.answer_a = ans_a

print(f"b: {ans_b}")
puzzle.answer_b = ans_b