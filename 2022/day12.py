from aocd.models import Puzzle
import os, sys, heapq
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

class Point():
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.π = None
        self.d = sys.maxsize
        self.v = v

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __lt__(self, __o: object) -> bool:
        return self.d < __o.d

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Point):
            return False
        return self.x == __o.x and self.y == __o.y

def relax(u: Point, v: Point):
    if v.d > u.d + 1:
        v.d = u.d + 1
        v.π = u


puzzle = Puzzle(year=2022, day=12)
data = puzzle.example_data
data = puzzle.input_data
data = [[ord(char) for char in line] for line in data.split("\n")]
data = [[Point(j, i, data[j][i]) for i in range(len(data[0]))] for j in range(len(data))]

for row in range(len(data)): #parsing start, end, and path_info
    for col in range(len(data[row])):
        if data[row][col].v == ord('S'):
            data[row][col].v = ord('a')
            start = data[row][col]
        elif data[row][col].v == ord('E'):
            data[row][col].v = ord('z')
            data[row][col].d = 0
            end = data[row][col]

q = list()
s = list()
for line in data:
    for point in line:
        q.append(point)
heapq.heapify(q)
while len(q) > 0:
    curr = heapq.heappop(q)
    s.append(curr)
    if curr.x > 0 and curr.v - 1 <= data[curr.x - 1][curr.y].v:
        relax(curr, data[curr.x - 1][curr.y])
    if curr.x < len(data) - 1 and curr.v - 1 <= data[curr.x + 1][curr.y].v:
        relax(curr, data[curr.x + 1][curr.y])
    if curr.y > 0 and curr.v - 1 <= data[curr.x][curr.y - 1].v:
        relax(curr, data[curr.x][curr.y - 1])
    if curr.y < len(data[0]) - 1 and curr.v - 1 <= data[curr.x][curr.y + 1].v:
        relax(curr, data[curr.x][curr.y + 1])
    heapq.heapify(q)
    
As = list()
for line in data:
    for point in line:
        if point.v == ord('a'):
            As.append(point.d)



print(f"a: {start.d}")
#puzzle.answer_a = start.d

print(f"b: {min(As)}")
puzzle.answer_b = min(As)