import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

             #name       speed  time rest
reindeer: dict[str : tuple[int, int, int]] = {}
for line in data:
    line = line.split(" ")
    id = line[0]
    speed = int(line[3])
    time = int(line[6])
    rest = int(line[-2])
    reindeer[id] = (speed, time, rest)


def solution_a():
    TIME = 2503
    final = []
    for id, stats in reindeer.items():
        speed = stats[0]
        time = stats[1]
        rest = stats[2]
        final.append(TIME // (time + rest) * (speed * time) + ((speed * time) if TIME % (time + rest) >= time else ((TIME % (time + rest)) * speed)))
    return max(final)


def solution_b():
    TIME = 2503
    points = dict()
    for id in reindeer.keys():
        points[id] = 0
    for t in range(1, TIME + 1):
        curr = dict()
        for id, stats in reindeer.items():
            speed = stats[0]
            time = stats[1]
            rest = stats[2]
            curr[id] = t // (time + rest) * (speed * time) + ((speed * time) if t % (time + rest) >= time else ((t % (time + rest)) * speed))
        max_x = 0
        first_place = []
        for id, x in curr.items():
            if x > max_x:
                first_place = [id]
                max_x = x
            elif x == max_x:
                first_place.append(id)
        for deer in first_place:
            points[deer] += 1
    return points[max(points, key=points.get)]
print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

