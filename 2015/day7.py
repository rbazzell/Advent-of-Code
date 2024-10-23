import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

#NOTE for the example, the line 'x AND y -> d' was changed to be 'x AND y -> a' to allow the solution to work

class Gate:

    def __init__(self, id:str, command:str, input):
        self.id = id
        self.command = command
        self.input = input
        self.output = None
    
    def clear(self):
        self.output = None

    def compute(self, circuit):
        if self.output != None:
            return self.output
        
        input = list(self.input)
        for i in range(len(input)):
            if isinstance(input[i], str):
                input[i] = circuit[input[i]].compute(circuit)

        match self.command:
            case "ASSIGN":
                self.output = input[0]
            case "NOT":
                self.output = ~input[0]
            case "AND":
                self.output = input[0] & input[1]
            case "OR":
                self.output = input[0] | input[1]
            case "LSHIFT":
                self.output = input[0] << input[1]
            case "RSHIFT":
                self.output = input[0] >> input[1]
        return self.output
            
    def __repr__(self):
        match self.command:
            case "ASSIGN":
                return f"{self.input[0]} -> {self.id}"
            case "NOT":
                return f"{self.command} {self.input[0]} -> {self.id}"
            case _:
                return f"{self.input[0]} {self.command} {self.input[1]} -> {self.id}"
    
    def clear_all(circuit:dict):
        for gate in circuit.values():
            gate.clear()
    


data = data.split("\n")
circuit = dict()
for line in data:
    lhs, output = line.split(" -> ")
    lhs = lhs.split(" ")
    if lhs[0] == "NOT":
        if lhs[1].isdigit():
            lhs[1] = int(lhs[1])
        command = lhs[0]
        input = (lhs[1],)
    elif len(lhs) > 1:
        command = lhs[1]
        if lhs[0].isdigit():
            lhs[0] = int(lhs[0])
        if lhs[2].isdigit():
            lhs[2] = int(lhs[2])
        input = (lhs[0], lhs[2])
    else:
        command = "ASSIGN"
        if lhs[0].isdigit():
            lhs[0] = int(lhs[0])
        input = (lhs[0],)
    circuit[output] = Gate(output, command, input)
    


def solution_a():
    return circuit["a"].compute(circuit)

def solution_b():
    a = solution_a()
    circuit["b"] = Gate("b", "ASSIGN", (circuit["a"].output,))
    Gate.clear_all(circuit)
    return solution_a()

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

