import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

class Rule:
    def __init__(self, rule: str):
        rule = rule.split(" ")
        self.low_type = rule[5]
        self.low_dest = int(rule[6])
        self.high_type = rule[10]
        self.high_dest = int(rule[11])
    
    def __repr__(self) -> str:
        return f"low -> {self.low_type} {self.low_dest} | high -> {self.high_type} {self.high_dest}"

    def botputs(self, factory):
        bots = []
        if self.low_type == "bot" and factory[self.low_dest].is_full():
            bots.append(factory[self.low_dest])
        if self.high_type == "bot" and factory[self.high_dest].is_full():
            bots.append(factory[self.high_dest]) 
        return bots

class Robot:
    def __init__(self, id:int):
        self.id = id
        self.high = None
        self.low = None
        self.rule = None
    
    def give(self, value:int) -> None:
        if self.high == None and self.low == None:
            self.low = value
        elif self.high == None:
            self.high = max(self.low, value)
            self.low = min(self.low, value)

    def set_rule(self, rule: Rule) -> None:
        self.rule = rule

    def hand_off(self, factory: dict, outputs: dict, compare:bool=True) -> bool:
        low = self.low
        high = self.high

        if low == 17 and high == 61 and compare:
            return True

        if self.rule.low_type == "bot":
            if factory[self.rule.low_dest].is_full():
                factory[self.rule.low_dest].hand_off(factory, outputs)
            factory[self.rule.low_dest].give(low)
        else:
            outputs[self.rule.low_dest] = low

        if self.rule.high_type == "bot":
            if factory[self.rule.high_dest].is_full():
                factory[self.rule.high_dest].hand_off(factory, outputs)
            factory[self.rule.high_dest].give(high)
        else:
            outputs[self.rule.high_dest] = high
        
        self.right = None
        self.left = None
        return False
    
    def is_full(self) -> bool:
        return self.high != None and self.low != None
    
    def __repr__(self):
        return f"({self.id}: {self.low}, {self.high}, {self.rule})"

factory: dict[int : Robot] = dict()
outputs: dict[int : int] = dict()
for line in data:
    split_line = line.split(" ")
    if split_line[0] == "value": #gives a starting value
        if factory.get(int(split_line[-1])) == None:
            factory[int(split_line[-1])] = Robot(int(split_line[-1]))
        factory[int(split_line[-1])].give(int(split_line[1]))
    elif split_line[0] == "bot": #gives a giving rule
        rule = Rule(line)
        if factory.get(int(split_line[1])) == None:
            factory[int(split_line[1])] = Robot(int(split_line[1]))
        factory[int(split_line[1])].set_rule(rule)

def solution_a():
    stack :list[Robot] = []
    for robot in factory.values():
        if robot.is_full():
            stack.append(robot)
    
    while len(stack) > 0:
        robot = stack.pop()
        if robot.hand_off(factory, outputs):
            return robot.id
        stack.extend(robot.rule.botputs(factory))

def solution_b():
    stack :list[Robot] = []
    for robot in factory.values():
        if robot.is_full():
            stack.append(robot)
    
    while len(stack) > 0 and (outputs.get(0) == None or outputs.get(1) == None or outputs.get(2) == None):
        robot = stack.pop()
        robot.hand_off(factory, outputs, compare=False)
        stack.extend(robot.rule.botputs(factory))
    return outputs[0] * outputs[1] * outputs[2]

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

