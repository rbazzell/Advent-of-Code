import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

SEA_MONSTER = [(0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 0), (18, 1), (19, 1)]
    
puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n\n")

class Tile:
    def __init__(self, id, grid):
        self.id = id
        if isinstance(grid, str):
            self.grid = [[col for col in row] for row in grid.split("\n")]
        else:
            self.grid = grid
        self.eval_sides()
        self.x = None
        self.y = None

        self.rotation = 0
        self.flipped = True

    def flip(self): #flips grid vertically (about the x axis)
        self.flipped = not self.flipped
        self.grid = self.grid[::-1]
        self.eval_sides()
        return self

    def rotate(self): #rotates grid 90 cw
        self.rotation = (self.rotation + 1) % 4 
        self.grid = [[y for y in x] for x in list(zip(*self.grid[::-1]))]
        self.eval_sides()
        return self

    def eval_sides(self):
        self.top = self.grid[0]
        self.bottom = self.grid[-1]
        self.left = [row[0] for row in self.grid]
        self.right = [row[-1] for row in self.grid]
        self.sides = [self.top, self.right, self.bottom, self.left]
        
    
    def set_location(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return aocu.grid_str(self.grid)


tiles = {int(tile.split("\n")[0].split(" ")[1][:-1]) : Tile(int(tile.split("\n")[0].split(" ")[1][:-1]), tile.split(":\n")[1]) for tile in data}

def find_id(curr_id: int, side: list) -> int:
    for id, tile in tiles.items():
        if id == curr_id:
            continue #skip
        if side in tile.sides or side[::-1] in tile.sides:
            return id
    return -1 #should be -1 if no neighbor

def reorient(curr_side: int, target_side: int, tile_id: int, target_tile_id: int) -> None:
    target_tile = tiles[target_tile_id]
    tile = tiles[tile_id]
#    if ((curr_side in [0, 1] and target_side in [2, 3]) or (curr_side in [2, 3] and target_side in [0, 1])) and reversed:
#        tile.flip()
    offset = (curr_side - target_side) % 4 - 2
    while offset != 0:
        tile.rotate()
        curr_side = (curr_side + 1) % 4
        offset = (curr_side - target_side) % 4 - 2
    if tile.sides[curr_side] != target_tile.sides[target_side]:
        tile.flip()
        if (target_side % 2) == 0:
            tile.rotate().rotate()
    


def solution_a():
    id = list(tiles.keys())[0]
    tile = tiles[id]
    tile.set_location(0,0)

    tile_queue = [(id, tile)]

    while len(tile_queue) > 0:
        id, tile = tile_queue.pop()
        for s, side in enumerate(tile.sides):
            # for s, 0 = top, 1 = right, 2 = bottom, 3 = left
            neighbor_id = find_id(id, side)
            
            if neighbor_id == -1 or tiles[neighbor_id].x != None:
                continue #skip, this side is an edge
            neighbor = tiles[neighbor_id]
            for ns, neighbor_side in enumerate(tiles[neighbor_id].sides):
                if side == neighbor_side:
                    reorient(ns, s, neighbor_id, id)
                    break
                if side == neighbor_side[::-1]:
                    reorient(ns, s, neighbor_id, id)
                    break
            match s:
                case 0:
                    neighbor.set_location(tile.x, tile.y + 1)
                case 1:
                    neighbor.set_location(tile.x + 1, tile.y)
                case 2:
                    neighbor.set_location(tile.x, tile.y - 1)
                case 3:
                    neighbor.set_location(tile.x - 1, tile.y)
            tile_queue.append((neighbor_id, neighbor))

    x_max = y_max = 0
    x_min = y_min = 400000000

    for id, tile in tiles.items():
        if tile.x > x_max:
            x_max = tile.x
        if tile.y > y_max:
            y_max = tile.y
        if tile.x < x_min:
            x_min = tile.x
        if tile.y < y_min:
            y_min = tile.y


    picture = [[0 for i in range(x_min, x_max + 1)] for j in range(y_min, y_max + 1)]
    for id, tile in tiles.items():
        tile.flip() # needed so orientation is correct in picture
        picture[tile.y - y_min][tile.x - x_min] = id

    tiles[0] = (Tile(0, [["0" for i in range(10)] for j in range(10)]))

    image = ""
    for r in range(len(picture)):
        for i in range(len(tiles[picture[r][0]].grid)):
            for c in range(len(picture[r])):
                for character in tiles[picture[r][c]].grid[i]:
                    image += character
                image += " "
            image += "\n"
        image += "\n"

    return image, picture[0][0] * picture[0][-1] * picture[-1][0] * picture[-1][-1] #4 corners


def check_sea_monster(image, r:int, c:int) -> bool:
    sea_monster_found = True
    for x, y in SEA_MONSTER:
        sea_monster_found = sea_monster_found and image[r + y][c + x] == "#"
    return sea_monster_found


def set_sea_monster(image:list[str], r:int, c:int) -> None:
    for x, y in SEA_MONSTER:
        image[r + y][c + x] = "O"


def count_hash(image:list[str]) -> int:
    roughness = 0
    for row in image:
        roughness += row.count("#")
    return roughness


def remove_borders(image:list[str]) -> None:
    #remove every column where i = 10n or i = 10n-9
    #start at len(image) so it doesn't mess up indexing as you remove
    for i in range(len(image)-1 , 0, -10):        
        image.pop(i)
        image.pop(i-9)   
        #remove every row where i = 10n or i = 10n-9
        #start at len(image) so it doesn't mess up indexing as you remove

    for i in range(len(image)):
        for j in range(len(image[i])-1, 0, -10):
                image[i] = image[i][:j] + image[i][j+1:]
                image[i] = image[i][:j-9] + image[i][j-9+1:]
    


def solution_b(image):
    image = image.replace(" ", "").replace("\n\n", "\n").split("\n")[:-1]
    remove_borders(image)
    
    correct_orientation = False
    for flip in range(2):
        for orientation in range(4):
            print(f"{orientation*90}deg | flipped?: {bool(flip)}")
            aocu.print_grid(image)
            print()
            for r in range(len(image) - 3):
                for c in range(len(image[r]) - 20):
                    sea_monster_found = check_sea_monster(image, r, c)
                    correct_orientation = correct_orientation or sea_monster_found
                    if sea_monster_found:
                        set_sea_monster(image, r, c)
            if correct_orientation:
                return count_hash(image)
            image = [[y for y in x] for x in list(zip(*image[::-1]))]
        image = image[::-1]
            
            

image, ans_a = solution_a()
ans_b = solution_b(image)
print(ans_b)
#puzzle.answer_a = ans_a
puzzle.answer_b = ans_b

