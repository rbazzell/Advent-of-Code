import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = [int(x) for x in data]

class Circle:
    class Node:
        def __init__(self, key: int):
            self.key = key
            self.right = None
        
        def __repr__(self) -> str:
            return str(self.key)

    def __init__(self, l: list[int]):
        self.size = len(l)
        self.head = self.Node(l[0])
        self.dictionary = {l[0] : self.head}
        curr = self.head
        prev = None
        for i in range(1, len(l)):
            prev = curr
            curr = self.Node(l[i])
            prev.right = curr
            self.dictionary[l[i]] = curr
        curr.right = self.head

    def __repr__(self) -> str:
        result = str(self.head) + " "
        curr = self.head.right
        while curr != self.head:
            result += str(curr) + " "
            curr = curr.right
        return result[:-1]

    def pick_up(self, current_cup: int) -> list[Node]:
        curr = self.dictionary[current_cup]
        up_cups = [curr.right, curr.right.right, curr.right.right.right]
        curr.right = up_cups[-1].right
        up_cups[2].right = None
        return up_cups
    
    def find_destination(self, current_cup: int, up_cups: list[Node]) -> Node:
        destination_label = (current_cup - 2) % self.size + 1
        while self.dictionary[destination_label] in up_cups:
            destination_label = (self.dictionary[destination_label].key - 2) % self.size + 1
        return self.dictionary[destination_label]

    def insert_cups(self, destination: Node, up_cups: list[Node]) -> None:
        #places the cups in and adjusts left and right pointers
        far_right = destination.right
        destination.right = up_cups[0]
        up_cups[-1].right = far_right

    def do_crab_move(self):
        up_cups = self.pick_up(self.head.key)
        destination = self.find_destination(self.head.key, up_cups)
        self.insert_cups(destination, up_cups)
        self.head = self.head.right

    def give_order(self) -> str:
        order = ""
        one = self.dictionary[1]
        curr = one.right
        while curr.key != 1:
            order += str(curr.key)
            curr = curr.right
        return order

def solution_a():
    cups = Circle(data)
    
    for iter in range(100):
        cups.do_crab_move()
    
    return cups.give_order()

def solution_b():
    cups = data.copy() + [x for x in range(max(data) + 1, 1000000 + 1)]
    cups = Circle(cups)

    for iter in range(10000000):
        cups.do_crab_move()

    one = cups.dictionary[1]
    return one.right.key * one.right.right.key

print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

