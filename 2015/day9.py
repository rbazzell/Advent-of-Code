import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

class Graph:
    class Node:
        def __init__(self, id:str):
            self.id = id
            self.edges = dict()
            self.visited = False

        def add_edge(self, destination, weight:int):
            self.edges[destination.id] = weight

        def del_edge(self, destination):
            del self.edges[destination.id]

        def __repr__(self):
            return self.id

        def __eq__(self, other):
            if isinstance(other, Graph.Node):
                return other.id == self.id
            elif isinstance(other, str):
                return other == self.id
            return False

        def visit(self):
            self.visited = True

        def unvisit(self):
            self.visited = False
        
    def __init__(self):
        self.nodes = {}

    def add_node(self, id:str):
        if self.nodes.get(id) == None:
            self.nodes[id] = Graph.Node(id)

    def unvisit_all(self):
        for node in self.nodes.values():
            node.unvisit()

    def node(self, id:str) -> Node:
        return self.nodes[id]
    
    def add_edge(self, id1:str, id2:str, weight:int):
        node1 = self.nodes[id1]
        node2 = self.nodes[id2]
        node1.add_edge(node2, weight)
        node2.add_edge(node1, weight)
            
    def shortest_path(self):
        shortest_path = 2147483647
        for node in self.nodes.values():
            visited = [node.id]
            shortest_path = min(shortest_path, *self.paths(node, visited))
        return shortest_path

    def longest_path(self):
        longest_path = 0
        for node in self.nodes.values():
            visited = [node.id]
            longest_path = max(longest_path, *self.paths(node, visited))
        return longest_path

    def paths(self, node, visited):
        weights = []
        for dest, weight in node.edges.items():
            if dest not in visited:
                if len(visited) == len(self.nodes) - 1:
                    weights.append(weight)
                weights.extend([weight + x for x in self.paths(self.nodes[dest], visited + [dest])])
        return weights
        

                    


        


data = data.split("\n")

graph = Graph()
for line in data:
    line = line.split(" ") #0,2 are locations, -1 is weight
    graph.add_node(line[0])
    graph.add_node(line[2])
    graph.add_edge(line[0], line[2], int(line[-1]))




def solution_a():
    return graph.shortest_path()

def solution_b():
    return graph.longest_path()

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()
