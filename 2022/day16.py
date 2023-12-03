from aocd.models import Puzzle
from typing import Self
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f1428a3a30e1aa3bd9c5faf951111cb16edaa38584883f8c4c0015a743934190eecaf1db7e0bb821b3168d590e18f9090193f56c1a1e14cd2"  # handout: exclude

puzzle = Puzzle(year=2022, day=16)
data = puzzle.example_data
#data = puzzle.input_data

class Room:
    def __init__(self: Self, name: str, adj: tuple[str], f: int) -> Self:
        self.name = name
        self.adj = adj
        self.f = f
        self.distances: dict[Room, int] = dict()

    def distance(self: Self, room: Self) -> int:
        if room not in self.distances:
            self.distances[room] = Room.calc_distance(self, room)
        return self.distances[room]

    def __repr__(self: Self) -> str:
        return f"[{self.name}, {self.f}]"
    
    def calc_distance(start: Self, end: Self) -> int:
        pass # put dijkstras here, found in day12(2022)

    def matches_name(self: Self, name: str) -> bool:
        return self.name == name
    
    def adjust_adjacencies(self: Self, rooms: list[Self]): 
        new_adj: list[Room] = list()
        for adj_room in self.adj:
            for room in rooms:
                if room.matches_name(adj_room):
                    new_adj.append(room)
                    break
        self.adj = tuple(new_adj)


def parse(data):
    rooms: list[Room] = list()
    for line in data.split("\n"):
        l = line.split(" ")
        adj = line.split(", ")
        adj[0] = adj[0][-2:]
        rooms.append(Room(l[1], tuple(adj), int(l[4][5:-1])))
    for room in rooms:
        room.adjust_adjacencies(rooms)
    return rooms
    
    



def part_a():
    pass

def part_b():
    pass

rooms: list[Room] = parse(data)
ans_a = part_a()
print(f"a: {ans_a}")
#puzzle.answer_a = ans_a

ans_b = part_b()
print(f"b: {ans_b}")
#puzzle.answer_b = ans_b