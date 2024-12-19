import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
#data = \
"""#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^<^^>v>>"""
data = input_data

data = data.split("\n\n")
warehouse = [list(x) for x in data[0].split("\n")]
movements = "".join(data[1].split("\n"))


def solution_a():
    start = None
    boxes = set()
    walls = set()
    for r, row in enumerate(warehouse):
        for c, spot in enumerate(row):
            if spot == "@":
                start = (r, c)
            elif spot == "O":
                boxes.add((r, c))
            elif spot == "#":
                walls.add((r, c))

    r, c = start
    for move in movements:
        dr, dc = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}[move]
        if (r + dr, c + dc) in boxes:
            move = True
            boxes_to_move = set()
            n = 1
            while move and (r + n*dr, c + n*dc) in boxes:
                boxes_to_move.add((r + n*dr, c+n*dc))
                n += 1
                if (r + n*dr, c + n*dc) in walls:
                    move = False
            if move:
                boxes.difference_update(boxes_to_move)
                for br, bc in boxes_to_move:
                    boxes.add((br+dr, bc+dc))
                r, c = r + dr, c + dc
        elif (r + dr, c + dc) not in walls:
            r, c = r + dr, c + dc

    total_gps = 0
    for r, c in boxes:
        total_gps += 100 * r + c
    return total_gps
        
    
def solution_b():
    start = None
    boxes = set()
    walls = set()
    for r, row in enumerate(warehouse):
        for c, spot in enumerate(row):
            if spot == "@":
                start = (r, 2*c)
            elif spot == "O":
                boxes.add((r, 2*c))
            elif spot == "#":
                walls.add((r, 2*c))
                walls.add((r, 2*c + 1))
    print(f"Initial state:\n{to_warehouse(boxes, walls, start, True)}\n")

    r, c = start
    for move in movements:
        if (r, c) == (8, 8) and move == "v":
            pass
        dr, dc = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}[move]
        if {(r + dr, c + dc), (r + dr, c + dc - 1)} & boxes: #need better check
            can_move = True
            boxes_to_move = {(r + dr, c + dc), (r + dr, c + dc - 1)} & boxes
            
            q = list(boxes_to_move)
            if move in ("^", "v"):
                while can_move and q:
                    br, bc = q.pop()
                    boxes_to_move.add((br, bc))
                    if {(br + dr, bc), (br + dr, bc + 1)} & walls:
                        can_move = False
                    else:
                        q.extend({(br + dr, bc - 1), (br + dr, bc), (br + dr, bc + 1)} & boxes)
            else:
                while can_move and q:
                    br, bc = q.pop()
                    boxes_to_move.add((br, bc))
                    if {(br, bc + dc), (br, bc + dc + 1)} & walls:
                        can_move = False
                    elif (br, bc + 2*dc) in boxes:
                        q.append((br, bc + 2*dc))
            if can_move:
                boxes.difference_update(boxes_to_move)
                for br, bc in boxes_to_move:
                    boxes.add((br+dr, bc+dc))
                r, c = r + dr, c + dc
        elif (r + dr, c + dc) not in walls:
            r, c = r + dr, c + dc

    total_gps = 0
    for br, bc in boxes:
        total_gps += 100 * br + bc
    return total_gps


#only here for debugging
def to_warehouse(boxes: set[tuple[int]], walls:set[tuple[int]], robot: tuple[int], wide: bool=False):
    s = ""
    in_box = False
    for r in range(max(walls)[0]+1):
        for c in range(max(walls)[1]+1):
            if (r, c) in walls:
                s += "#"
            elif (r, c) in boxes:
                if wide:
                    s += "["
                else:
                    s += "O"
                in_box = True
            elif wide and in_box:
                s += "]"
                in_box = False
            elif (r, c) == robot:
                s += "@"
            else:
                s += "."
        s += "\n"
    return s[:-1]


print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

