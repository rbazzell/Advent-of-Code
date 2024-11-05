import sys
from itertools import combinations
from collections import deque
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

class Item:
    def __init__(self, id: str, type: str):
        self.id = id
        self.type = type

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.id == other.id and self.type == other.type
        return False
    
    def __hash__(self):
        return hash((self.id, self.type))
    
    def __repr__(self):
        return f"{self.id} {self.type[0]}"

class Floor:
    def __init__(self, contents: str):
        self.items = []
        self.pairs = 0
        self.microchips = 0
        self.generators = 0
        contents = contents.split(", ")
        if len(contents) == 1:
            contents = contents[0].split(" and ")
        if len(contents) != 1 or contents[0] != "nothing relevant.":
            for item in contents:
                item = item.split(" ")[1:] #cuts off the 'a ' at the beginning
                if item[0] == "a":
                    item = item[1:]
                type = item[1].strip(".")
                id = item[0][:2]
                self.give_item(Item(id, type))

    def count_items(self) -> int:
        return len(self.items)
    
    def take_item(self, item: Item) -> None:
        self.items.remove(item)
        if item.type == "microchip":
            self.microchips -= 1
            if Item(item.id, "generator") in self.items:
                self.pairs -= 1
        else:
            self.generators -= 1
            if Item(item.id, "microchip") in self.items:
                self.pairs -= 1
    
    def give_item(self, item: Item) -> None:
        self.items.append(item)
        if item.type == "microchip":
            self.microchips += 1
            if Item(item.id, "generator") in self.items:
                self.pairs += 1
        else:
            self.generators += 1
            if Item(item.id, "microchip") in self.items:
                self.pairs += 1

    def validate(self) -> bool:
        #as many chips, but no gens OR no unpaired chips
        return self.generators == 0 or self.microchips - self.pairs == 0

    def copy(self):
        floor = Floor("nothing relevant.")
        floor.items = self.items.copy()
        floor.microchips = self.microchips
        floor.generators = self.generators
        floor.pairs = self.pairs
        return floor

    def __eq__(self, other) -> bool:
        return self.__hash__() == other.__hash__()
    
    def __repr__(self) -> str:
        microchips = [item.id for item in self.items if item.type == "microchip"]
        generators = [item.id for item in self.items if item.type == "generator"]
        return f"(g:{generators}, m:{microchips})"
    
    def __hash__(self):
        return hash((self.microchips, self.generators, self.pairs))

class Elevator:
    def __init__(self, building: dict[int, Floor]):
        self.floor = 1
        self.building = {x : y.copy() for x, y in building.items()}

    def copy(self):
        elevator = Elevator(self.building)
        elevator.floor = self.floor
        return elevator

    def move(self, direction: str, combo: list[str]) -> None:
        if direction == "up":
            next_floor = self.floor + 1
        else:
            next_floor = self.floor - 1

        for item in combo:
            self.building[self.floor].take_item(item)
            self.building[next_floor].give_item(item)
        self.floor = next_floor

    def can_move(self, direction):
        if direction == "up":
            return self.floor != 4
        else:
            return self.floor != 1

    def validate_building(self) -> bool:
        for i in range(1, 5):
            if not self.building[i].validate():
                return False
        return True

    def final(self):
        return self.floor == 4 and len(self.building[1].items) == 0 and len(self.building[2].items) == 0 and len(self.building[3].items) == 0

    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Elevator):
            return False
        return self.__hash__() == other.__hash__()


    def __repr__(self) -> str:
        return f"F{self.floor}"
        

    def __hash__(self):
        hash_floors = tuple(floor for floor in self.building.values())
        return hash((self.floor, hash_floors))

 
items = 0
initial_state = dict()
for i, line in enumerate(data):
    line = line.split(" contains ")[1]
    initial_state[i+1] = Floor(line)

def moves(elevator: Elevator, direction: str):
    yielded = False
    current_floor = elevator.building[elevator.floor]

    items_to_move = 2 if direction == "up" else 1
    for combo in combinations(current_floor.items, items_to_move):
        trial = elevator.copy()
        trial.move(direction, combo)

        if trial.validate_building():
            yielded = True
            yield trial

    if not yielded and direction == "up":
        for combo in combinations(current_floor.items, 1):
            trial = elevator.copy()
            trial.move(direction, combo)

            if trial.validate_building():
                yielded = True
                yield trial
    #THIS CASE IS NOT NEEDED FOR MOST INPUTS (removing saves ~0.25s)
    elif not yielded and direction == "down":
        for combo in combinations(current_floor.items, 2):
            trial = elevator.copy()
            trial.move(direction, combo)

            if trial.validate_building():
                yielded = True
                yield trial



def min_steps(elevator: Elevator) -> int:
    queue = deque([(elevator, 0)])
    visited = {elevator}

    while queue:
        curr_elevator, steps = queue.popleft()

        if curr_elevator.final():
            return steps
        
        #if not, explore possible moves
        for direction in ["up", "down"]:
            if curr_elevator.can_move(direction):
                for new_elevator in moves(curr_elevator, direction):
                    if new_elevator not in visited:
                        visited.add(new_elevator)
                        queue.append((new_elevator, steps + 1))
    return -1 #base case - SHOULD NEVER GET HERE

def solution_a():
    building = initial_state.copy()
    elevator = Elevator(building)
    return min_steps(elevator)

def solution_b():
    building: dict[int, Floor] = initial_state.copy()
    for id in ("elerium", "dilithium"):
        for type in ("generator", "microchip"):
            building[1].give_item(Item(id, type))
    elevator = Elevator(building)
    return min_steps(elevator)

import time
start = time.time()

print(solution_b())

end = time.time()

print(f"Time: {round(end - start, 6)} s")
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

