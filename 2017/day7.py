import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data


class Graph:
    def __init__(self, S: str):
        self.vertices: dict[str, int] = dict()
        self.children: dict[str, list[str]] = dict()
        self.parents: dict[str, str] = dict()
        for line in S.split("\n"):
            line = line.split(" -> ")
            vertex = line[0]
            if len(line) > 1:
                children = line[1].split(", ")
            else:
                children = []

            v_id, v_weight = vertex.split(" ")
            v_weight = int(v_weight[1:-1]) #removes parens
            self.vertices[v_id] = v_weight

            if children:
                self.children[v_id] = list()
                for child in children:
                    self.children[v_id].append(child)
                    self.parents[child] = v_id
        
        self.root: str = ""
        for v in self.children.keys():
            if not self.parents.get(v):
                self.root = v
                break
        self.towers = dict()
       
    def __tower_weights(self, v: str):
        if not self.towers.get(v):
            weights = self.vertices[v]
            if self.children.get(v):
                for c in self.children[v]:
                    weights += self.__tower_weights(c)
            self.towers[v] = weights
        return self.towers[v]
    
    def find_unbalanced_disk(self):
        if not self.towers:
            self.__tower_weights(self.root)
        return self.__unbalanced(self.root)


    def __unbalanced(self, v: str):
        if not self.children.get(v):
            return v
        c_costs_list = {c: self.towers[c] for c in self.children[v]}
        c_costs_types = set(c_costs_list.values())

        if len(c_costs_types) == 1:
            return v
        else:
            c_costs_counts = {cost: list(c_costs_list.values()).count(cost) for cost in c_costs_list.values()}
            unbalanced_cost = min(c_costs_counts, key=c_costs_counts.get)
            c = ""
            for child, weight in c_costs_list.items():
                if weight == unbalanced_cost:
                    c = child
                    break
            return self.__unbalanced(c)
        
    def adjust_weight(self, v: str):
        p = self.parents[v]
        sibs = self.children[p]
        sib_weight = (self.towers[p] - self.vertices[p] - self.towers[v]) // (len(sibs) - 1)
        return self.vertices[v] - (self.towers[v] - sib_weight )
        
            
        
            
    
            





def solution_a():
    stacks = Graph(data)
    return stacks.root

def solution_b():
    stacks = Graph(data)
    unbalanced_vertex = stacks.find_unbalanced_disk()
    print(unbalanced_vertex)
    return stacks.adjust_weight(unbalanced_vertex)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

