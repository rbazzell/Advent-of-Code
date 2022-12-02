from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=6)
data = puzzle.input_data
data = [int(x) for x in data.split(",")]


def simulate(lantern_fish, days):
    for day in range(days):
        temp = lantern_fish[0]
        for i in range(len(lantern_fish) - 1):
            lantern_fish[i] = lantern_fish[i + 1]
        lantern_fish[8] = temp
        lantern_fish[6] += temp
    return sum(lantern_fish)


lantern_fish = [0 for i in range(9)]
for num in data:
    lantern_fish[num] += 1


result_a = simulate(lantern_fish.copy(), 80)
result_b = simulate(lantern_fish.copy(), 256)

puzzle.answer_a = result_a
print(f"Part 1: {result_a}")
puzzle.answer_b = result_b
print(f"Part 2: {result_b}")