from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=3)
data = [[int(x) for x in [*line]] for line in puzzle.input_data.split("\n")]
# data = [[int(x) for x in [*line]] for line in puzzle.example_data.split("\n")]


column_totals = [0] * len(data[0])
for i in range(len(data[0])):
    for j in range(len(data)):
        column_totals[i] += data[j][i]

gamma = 0

for i in range(len(column_totals)):
    if column_totals[i] > len(data) // 2:
        gamma += 1 << (len(column_totals) - i - 1)
        
epsilon = gamma ^ 0xFFF
# puzzle.answer_a = epsilon * gamma
print(f"Part 1: {epsilon * gamma}")

oxygen = [int(x, 2) for x in puzzle.input_data.split("\n")]
co2 = oxygen.copy()

for i in range(len(data[0]) - 1, -1, -1):
    if len(oxygen) - 1:
        og_o2 = oxygen.copy()
        ones_o2 = 0
        for num in oxygen:
            if num & (1 << i):
                ones_o2 += 1
        for num in og_o2:
            if ones_o2 >= len(og_o2) / 2 and not num & (1 << i):
                oxygen.remove(num)
            elif ones_o2 < len(og_o2) / 2 and num & (1 << i):
                oxygen.remove(num)
    if len(co2) - 1:
        og_co2 = co2.copy()
        zeros_co2 = 0
        for num in co2:
            if not num & (1 << i):
                zeros_co2 += 1
        for num in og_co2:
            if zeros_co2 <= len(og_co2) / 2 and num & (1 << i):
                co2.remove(num)
            elif zeros_co2 > len(og_co2) / 2 and not num & (1 << i):
                co2.remove(num)
puzzle.answer_b = oxygen[0] * co2[0]
print(f"Part 2: {oxygen[0] * co2[0]}")
    
