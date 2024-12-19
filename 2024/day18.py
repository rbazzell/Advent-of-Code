import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
from heapq import heapify, heappush, heappop
from time import time

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data, size, first = examples[0].input_data, 7, 12
data, size, first = input_data, 71, 1024

data = data.split("\n")

first_kilo = set((int(line.split(",")[0]), int(line.split(",")[1])) for line in data[:first])
the_rest = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in data[first:]]

class Graph:
    class Vertex:
        def __init__(self, r: int, c: int):
            self.r: int = r
            self.c: int = c
            self.prev: set[tuple[int]] = None
            self.d: int = 2147483647
        
        def reset(self):
            self.prev: set[tuple[int]] = None
            self.d: int = 2147483647

        def adjacents(self):
            return {(self.r + 1, self.c), (self.r - 1, self.c), (self.r, self.c + 1), (self.r, self.c - 1)}

        def __repr__(self):
            return str((self.r, self.c))
        
        def __hash__(self):
            return hash((self.r, self.c))
        
        def __eq__(self, other):
            return isinstance(other, Graph.Vertex) and (self.r, self.c) == (other.r, other.c)
    
        def __lt__(self, other):
            return self.d < other.d


    def __init__(self, blocked, size):
        translate: dict[tuple[int], Graph.Vertex] = dict()
        self.vertices = set()
        for r in range(size):
            for c in range(size):
                if (r, c) not in blocked:
                    v = Graph.Vertex(r, c)
                    if r == 0 and c == 0:
                        self.start = v
                    if r == size - 1 and c == size - 1:
                        self.end = v
                    translate[(r, c)] = v
                    self.vertices.add(v)

        self.adj = dict()
        for p, v in translate.items():
            r, c = p
            self.adj[v] = dict()
            for ar, ac in v.adjacents() - blocked:
                if 0 <= ar < size and 0 <= ac < size:
                    self.adj[v][translate[(ar, ac)]] = 1

    def block(self, r, c):
        v = Graph.Vertex(r, c)
        self.vertices -= {v}
        if v in self.adj:
            for a in self.adj[v].keys():
                del self.adj[a][v]
            del self.adj[v]
        return v
    
    def initialize_single_source(self):
        for v in self.vertices:
            v.reset()
        self.start.d = 0

    def relax(self, v: Vertex, u: Vertex):
        if v.d > u.d + self.adj[u][v]:
            v.d = u.d + self.adj[u][v]
            v.prev = u

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
        return self.end.d

    def shortest_path(self):
        path = list()
        v = self.end
        while v.prev != None:
            path.append(v)
            v = v.prev
        return path

def solution_a():
    g = Graph(first_kilo, size)
    g.dijkstras()
    return g.shortest_path_weight()


def solution_b():
    g = Graph(first_kilo, size)
    g.dijkstras()
    path = g.shortest_path()
    i = -1
    while g.shortest_path_weight() != 2147483647 and i < len(the_rest) - 1:
        i += 1
        b = g.block(*the_rest[i])
        if b in path:
            g.dijkstras()
            path = g.shortest_path()
    return the_rest[i]



print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

