from aocd.models import Puzzle
from tqdm import tqdm
import os, operator
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=11)
data = puzzle.example_data
data = puzzle.input_data
data = data.split("\n\n")

class Monkey:
    OPS = {
        '+' : operator.add,
        '*' : operator.mul,
        '**' : operator.pow
    }
    shortener = 1
    relief = 3

    def __init__(self, starting_items, operation, test, iftrue, iffalse):
        self.items = starting_items # list of numbers
        self.operation = operation # tuple (operator, value)
        self.condition = test # number, since always "divisible"
        self.iftrue = iftrue # number of monkey
        self.iffalse = iffalse # number of monkey
        self.inspected = 0

    def inspect(self, monkeys):
        while len(self.items) > 0:
            item = self.items.pop()
            self.inspected += 1
            item = self.operate(item % Monkey.shortener) // Monkey.relief
            monkeys[self.test(item)].add_item(item)

    def operate(self, item):
        return Monkey.OPS[self.operation[0]](item, self.operation[1])

    def test(self, item):
        return self.iftrue if item % self.condition == 0 else self.iffalse

    def add_item(self, item):
        self.items.append(item)
    
    def parse(monkey):
        monkey = monkey.split("\n")
        items = [int(x.strip(",")) for x in monkey[1].split(" ")[4:]]
        operation = monkey[2][23:]
        match operation[0]:
            case "*":
                if operation[2:].isdigit():
                    operation = ('*', int(operation[2:]))
                else:
                    operation = ('**', 2)
            case "+":
                operation = ('+', int(operation[2:]))
        test = int(monkey[3][21:])
        iftrue = int(monkey[4][-1])
        iffalse = int(monkey[5][-1])
        return Monkey(items, operation, test, iftrue, iffalse)       
    
    def calc_shortener(monkeys):
        for monkey in monkeys:
            Monkey.shortener *= monkey.condition

    def set_relief(num):
        Monkey.relief = num
    
monkeys = [Monkey.parse(monkey) for monkey in data]
Monkey.calc_shortener(monkeys) #NEEDS THIS to prevent overflows
Monkey.set_relief(3)
for i in range(20):
    for monkey in monkeys:
        monkey.inspect(monkeys)

monkey_business = sorted(monkeys, key=lambda x:x.inspected, reverse=True)[0].inspected * sorted(monkeys, key=lambda x:x.inspected, reverse=True)[1].inspected

monkeys = [Monkey.parse(monkey) for monkey in data]
Monkey.set_relief(1)
for i in range(10000):
    for monkey in monkeys:
        monkey.inspect(monkeys)
    if i + 1 == 1:
        pass
    if i + 1 == 20:
        pass
    if i + 1 == 1000:
        pass
    if i + 1 == 2000:
        pass
    if i + 1 == 3000:
        pass
    if i + 1 == 4000:
        pass


simean_shenanigans = sorted(monkeys, key=lambda x:x.inspected, reverse=True)[0].inspected * sorted(monkeys, key=lambda x:x.inspected, reverse=True)[1].inspected


print(f"a: {monkey_business}")
#puzzle.answer_a = monkey_business

print(f"b: {simean_shenanigans}")
puzzle.answer_b = simean_shenanigans