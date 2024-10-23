import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(24, 2020)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

class Tile:
    TILES = dict()
    BLACK = 1
    WHITE = 0

    def __new__(cls, q:int, r:int, color:int):
        #check if a Tile with the same q and r already exists:
        if cls.TILES.get(q) != None and cls.TILES[q].get(r) != None:
            tile = cls.TILES[q][r]
            if color == Tile.BLACK:
                tile.flip()
            return tile
        
        #if not, create a new instance
        instance = super().__new__(cls)
        return instance

    
    def __init__(self, q:int, r:int, color:int):
        #prevents re-initialization
        if not hasattr(self, 'initialized'):
            # using coords from https://www.redblobgames.com/grids/hexagons/
            self.q = q
            self.r = r
            self.color = color
            
            #add to dicitonary in new location
            if Tile.TILES.get(self.q) == None:
                Tile.TILES[self.q] = dict()
            Tile.TILES[self.q][self.r] = self

            self.initialized = True #mark as initialized

    def flip(self):
        self.color = not self.color

    def black_neighbors(self):
        black_neighbors = 0
        for dq, dr in [(1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]:
            neighbor = Tile(self.q + dq, self.r + dr, Tile.WHITE)
            black_neighbors += neighbor.color
        return black_neighbors

    def __eq__(self, tile) -> bool:
        if not isinstance(tile, Tile):
            return False
        return self.q == tile.q and self.r == tile.r

    def __repr__(self) -> str:
        return f"[{self.q}, {self.r}], " + ("BLACK" if self.color else "WHITE")
    
    def __hash__(self):
        return hash((self.q, self.r))

    @classmethod
    def count_black(cls):
        black = 0
        for q in cls.TILES.values():
            for r in q.values():
                black += r.color
        return black
    
    @classmethod
    def black_tiles(cls):
        tiles = []
        for q in cls.TILES.values():
            for r in q.values():
                if r.color:
                    tiles.append(r)
        return tiles


paths = list()
for line in data:
    path = []
    two_char = False
    for i in range(len(line)):
        step = ""
        match line[i]:
            case 'n' | 's':
                two_char = True
            case 'e' | 'w':
                if two_char:
                    step = line[i-1] + line[i]
                    two_char = False
                else:
                    step = line[i] 
        if not two_char:
            path.append(step)
    paths.append(path)


def coordinates(path: list[str]) -> tuple[int]:
    q, r = 0, 0
    for command in path:
        match command: 
            case 'e': # +r = +q, -s
                q += 1
            case 'w': # -r = -q, +s
                q -= 1
            case 'ne': #+s = +q, -r
                q += 1
                r -= 1
            case 'sw': #-s = -q, +r
                q -= 1
                r += 1
            case 'se': #+q = +r, -s
                r += 1
            case 'nw': #-q = -r, +s
                r -= 1
    return q, r

def solution_a():
    for path in paths:
        q, r = coordinates(path)
        Tile(q, r, Tile.BLACK)
    return Tile.count_black()
        
        
# I think this is pretty close to as fast as possible, but it still takes a couple seconds to run
def solution_b():
    for path in paths:
        q, r = coordinates(path)
        Tile(q, r, Tile.BLACK)
    for day in range(100):
        b_tiles = Tile.black_tiles()
        flip_tiles = set()
        for b_tile in b_tiles:
            for dq, dr in [(0, 0),(1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]:
                tile = Tile(b_tile.q + dq, b_tile.r + dr, Tile.WHITE)
                b_neighbors = tile.black_neighbors()
                if tile.color == Tile.BLACK and (b_neighbors == 0 or b_neighbors > 2):
                    flip_tiles.add(tile)
                elif tile.color == Tile.WHITE and b_neighbors == 2:
                    flip_tiles.add(tile)
        for tile in list(flip_tiles):
            tile.flip()
    return Tile.count_black()




print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

