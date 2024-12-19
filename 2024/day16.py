import sys
from heapq import heappush, heappop, heapify
import heapq
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = \
"""#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
data = input_data

maze = tuple(tuple(line) for line in data.split("\n"))
start = None
end = None
opens = set()

class Graph:
    class Vertex:
        def __init__(self, r: int, c: int, dir: str):
            self.r: int = r
            self.c: int = c
            self.dir: str = dir
            self.prev: set[tuple[int]] = set()
            self.d: int = 2147483647
        
        def reset(self):
            self.prev: set[tuple[int]] = set()
            self.d: int = 2147483647

        def direction(self, v):
            return {(1, 0): "v", (-1, 0): "^", (0, 1): ">", (0, -1): "<"}[(v.r-self.r, v.c-self.c)]

        def __repr__(self):
            return str((self.r, self.c, self.dir))
        
        def __hash__(self):
            return hash((self.r, self.c, self.dir))
        
        def __eq__(self, other):
            return (isinstance(other, Graph) and other.id == self.id) or (isinstance(other, tuple) and other == self.id)
    
        def __lt__(self, other):
            return self.d < other.d

    def __init__(self, opens, start, end):
        self.adj = dict()
        translate = dict()
        self.start = Graph.Vertex(*start, ">")
        self.vertices = {self.start}
        translate[(*start, ">")] = self.start
        q = [(*start, ">")]
        while q:
            r, c, dir = q.pop(0)
            #create node if doesn't exist
            if (r, c, dir) not in translate:
                v = Graph.Vertex(r, c, dir)
                translate[(r, c, dir)] = v
                self.vertices.add(v)
            #grab node
            v = translate[(r, c, dir)]
            
            # if adjacencies have not already been set
            if v not in self.adj:
                self.adj[v] = dict()
                # add left rotation:
                left =  {"^": "<", "<": "v", "v": ">", ">": "^"}[dir]         
                q.append((r, c, left))
                if (r, c, left) not in translate:
                    u = Graph.Vertex(r, c, left)
                    translate[(r, c, left)] = u
                    self.vertices.add(u)
                u = translate[(r, c, left)]
                self.adj[v][u] = 1000

                # add right rotation:
                right = {"^": ">", ">": "v", "v": "<", "<": "^"}[dir]
                q.append((r, c, right))
                if (r, c, right) not in translate:
                    w = Graph.Vertex(r, c, right)
                    translate[(r, c, right)] = w
                    self.vertices.add(w)
                w = translate[(r, c, right)]
                self.adj[v][w] = 1000


                # add next position, same rotation, if exists
                dr, dc = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}[dir]
                nr, nc = r + dr, c + dc
                if (nr, nc) in opens:
                    q.append((nr, nc, dir))
                    if (nr, nc, dir) not in translate:
                        x = Graph.Vertex(nr, nc, dir)
                        translate[(nr, nc, dir)] = x
                        self.vertices.add(x)
                    x = translate[(nr, nc, dir)]
                    self.adj[v][x] = 1

        self.ends = {translate[(*end, d)] for d in "<>^v"}



    def initialize_single_source(self):
        for v in self.vertices:
            v.reset()
        self.start.d = 0

    def relax(self, v: Vertex, u: Vertex):
        if v.d > u.d + self.adj[u][v]:
            v.d = u.d + self.adj[u][v]
            v.prev = {u}
        elif v.d == u.d + self.adj[u][v]:
            v.prev.add(u)

    def dijkstras(self):
        self.initialize_single_source()
        self.start.d = 0
        q : list[Graph.Vertex] = list(self.vertices)
        heapify(q)
        while q:
            u = heappop(q)
            for v in self.adj[u].keys():
                b = v.d
                self.relax(v, u)
                a = v.d
                if a < b:
                    if v in q:
                        q.remove(v)
                    heappush(q, v)


    def shortest_path_weight(self):
        return min(e.d for e in self.ends)

    def shortest_path_all_possible(self):
        chairs = set()
        q = [e for e in self.ends if e.d == self.shortest_path_weight()]
        while q:
            e: Graph.Vertex = q.pop(0)
            chairs.add((e.r, e.c))
            for p in e.prev:
                q.append(p)
        return len(chairs)

for r, row in enumerate(maze):
    for c, spot in enumerate(row):
        match spot:
            case "S":
                start = (r, c)
                opens.add((r, c))
            case "E":
                end = (r, c)
                opens.add((r, c))
            case ".":
                opens.add((r, c))



def solution_a_fast():
    q = [(0, *start, ">")]
    visited = set()
    while q:
        score, r, c, dir = heappop(q)
        if (r, c) == end:
            return score
        visited.add((r, c))
        
        for dr, dc, ddir in ((0, 1, ">"), (0, -1, "<"), (1, 0, "v"), (-1, 0, "^")):
            if (r + dr, c + dc) in opens and (r + dr, c + dc) not in visited:
                if dir == ddir:
                    heappush(q, (score + 1, r + dr, c + dc, dir))
                else: #dir != ddir
                    heappush(q, (score + 1001, r + dr, c + dc, ddir))
    return -1

def solution_b_way_too_slow():
    optimal = solution_a()
    seats = {end}
    q = [(0, *start, ">", set())]
    while q:
        score, r, c, dir, path = heappop(q)
        if (r, c) == end:
            print("at end", end="")   
            if score == optimal:
                seats.update(path)
                print(" optimal")
            else:
                print()
        else:
            for dr, dc, ddir in ((0, 1, ">"), (0, -1, "<"), (1, 0, "v"), (-1, 0, "^")):
                if (r + dr, c + dc) in opens and (r + dr, c + dc) not in path:
                    if dir == ddir and score + 1 <= optimal:
                        heappush(q, (score + 1, r + dr, c + dc, dir, path | {(r, c)}))
                    elif dir != ddir and score + 1001 <= optimal:
                        heappush(q, (score + 1001, r + dr, c + dc, ddir, path | {(r, c)}))
    return len(seats)

def solution_a():
    g = Graph(opens, start, end)
    g.dijkstras()
    return g.shortest_path_weight()

def solution_b():
    g = Graph(opens, start, end)
    g.dijkstras()
    return g.shortest_path_all_possible()



    

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

