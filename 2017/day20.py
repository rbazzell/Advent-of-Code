import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[1].input_data
data = input_data

data = data.split("\n")
class Particle:
    def __init__(self, id: int, p:tuple, v:tuple, a:tuple):
        self.id = id
        self.px, self.py, self.pz = p
        self.vx, self.vy, self.vz = v
        self.ax, self.ay, self.az = a

    def __repr__(self):
        return str(self.id)

    def simulate(self, t: int):
        self.vx = self.ax * t
        return abs(self.ax * (t ** 2) // 2 + self.vx * t + self.px) + \
               abs(self.ay * (t ** 2) // 2 + self.vy * t + self.py) + \
               abs(self.az * (t ** 2) // 2 + self.vz * t + self.pz)

    def simulate_xyz(self, t: int):
        return int(self.ax * (t ** 2) / 2 + self.vx * t + self.px), \
               int(self.ay * (t ** 2) / 2 + self.vy * t + self.py), \
               int(self.az * (t ** 2) / 2 + self.vz * t + self.pz)
    
    def step(self):
        self.vx += self.ax 
        self.vy += self.ay
        self.vz += self.az

        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz

        return self.px, self.py, self.pz
    

ps: list[Particle] = []
for i, line in enumerate(data):
    line = line.split(", ")
    p, v, a = ((int (y) for y in x[3:-1].split(",")) for x in line)
    ps.append(Particle(i, p, v, a))


def solution_a():
    min_part = 9999999, None
    for particle in ps:
        if particle.simulate(1000) < min_part[0]:
            min_part = particle.simulate(1000), particle
    return min_part[1].id


def solution_b():
    particles = ps.copy()
    for t in range(100):
        positions: dict[tuple[int, int, int], list[Particle]] = {}
        collisions = set()
        for particle in particles:
            x, y, z = particle.step()
            if (x, y, z) not in positions:
                positions[(x, y, z)] = list()
            positions[(x, y, z)].append(particle)
        for _, position in positions.items():
            if len(position) > 1:
                collisions.update(position)
        particles = [p for p in particles if p not in collisions]
    return len(particles)
        
            

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

