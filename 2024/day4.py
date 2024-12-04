import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
data = input_data

data = data.split("\n")


def search_range(r, dr, c, dc):
    if dr < 0:
        r_range = (r, r-1, r-2, r-3)
    elif dr > 0:
        r_range = (r, r+1, r+2, r+3)
    else:
        r_range = (r, r, r, r)

    if dc < 0:
        c_range = (c, c-1, c-2, c-3)
    elif dc > 0:
        c_range = (c, c+1, c+2, c+3)
    else:
        c_range = (c, c, c, c)

    return zip(r_range, c_range)


def solution_a():
    count = 0
    for r, line in enumerate(data):
        for c, s in enumerate(line):
            if s == "X":
                for dr, dc in ((-3, -3), (-3, 0), (-3, 3), (0, 3), (3, 3), (3, 0), (3, -3), (0, -3)):
                    if 0 <= r + dr < len(data) and 0 <= c + dc < len(line):
                        test = "".join(data[nr][nc] for nr, nc in search_range(r, dr, c, dc))
                        if test == "XMAS":
                            count += 1
    return count
                


def solution_b():
    count = 0
    for r, line in enumerate(data):
        for c, s in enumerate(line):
            if s == "A" and 1 <= r < len(data)-1 and 1 <= c < len(line)-1:
                # check diagonals
                fslash = data[r+1][c-1] + "A" + data[r-1][c+1]
                bslash = data[r-1][c-1] + "A" + data[r+1][c+1]
                if (fslash == "MAS" or fslash[::-1] == "MAS") and (bslash == "MAS" or bslash[::-1] == "MAS"):
                    count += 1
                # check orthogonals
                horiz = data[r][c-1] + "A" + data[r][c-1]
                verti = data[r-1][c] + "A" + data[r+1][c]
                if (horiz == "MAS" or horiz[::-1] == "MAS") and (verti == "MAS" or verti[::-1] == "MAS"):
                    count +=1
    return count

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

