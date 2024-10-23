import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
data = input_data
data = data.split("\n\n")

fields = dict()
for item in data[0].split("\n"):
    item = item.split(": ")
    ranges = item[1].split(" or ")
    a = ranges[0].split("-")
    b = ranges[1].split("-")
    a = range(int(a[0]), int(a[1]) + 1)
    b = range(int(b[0]), int(b[1]) + 1)

    fields[item[0]] = (a, b)

my_ticket = [int(x) for x in data[1].split("\n")[1].split(",")]
tickets = [[int(x) for x in y.split(",")] for y in data[2].split(":\n")[1].split("\n")]
tickets.insert(0, my_ticket)

def solution_a() -> int:
    sum = 0
    for t in tickets:
        for v in t:
            if not valid(v):
                sum += v
    return sum

def valid(value: int) -> bool:
    for f in fields.values():
        if value in f[0] or value in f[1]:
            return True
    return False


def solution_b() -> int:
    invalid_tickets = []
    for t in tickets:
        for v in t:
            if not valid(v):
                invalid_tickets.append(t)
    for t in invalid_tickets:
        tickets.remove(t)

    rosetta = list()
    for i in range(len(my_ticket)):
        fs = valid_fields(tickets[0][i])
        for t in tickets:
            fs.intersection_update(valid_fields(t[i]))
        rosetta.append(fs)


    while sum([len(x) for x in rosetta]) > len(rosetta):
        for f1 in rosetta:
            for f2 in rosetta:
                if f1 == f2 or len(f1) == 1:
                    continue
                if len(f2) == 1 and f2.copy().pop() in f1:
                    f1 -= f2

        result = 1
        for i, r in enumerate(rosetta):
            if "departure" in r.copy().pop():
                result *= my_ticket[i]
    return result

def valid_fields(value: int) -> set[str]:
    fs = set()
    for f, r in fields.items():
        if value in r[0] or value in r[1]:
            fs.add(f)
    return fs



print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

