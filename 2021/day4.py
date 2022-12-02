from aocd.models import Puzzle

def check_winning_boards(marks):
    for i in range(len(marks)):
        if check_board(marks, i):
            return i
    return -1


def check_losing_boards(marks):
    for i in range(len(marks)):
        if not check_board(marks, i):
            return i
    return -1


def check_board(marks, board):
    for j in range(5):
        if marks[board][j][0] + marks[board][j][1] + marks[board][j][2] + marks[board][j][3] + marks[board][j][4] == 5:
            return 1
        if marks[board][0][j] + marks[board][1][j] + marks[board][2][j] + marks[board][3][j] + marks[board][4][j] == 5:
            return 1
    return 0


def mark_boards(boards, marks, num):
    for i in range(len(boards)):
        for j in range(5):
            for k in range(5):
                if boards[i][j][k] == num:
                    marks[i][j][k] = 1


def sum_board(boards, marks, board):
    sum = 0
    for i in range(5):
        for j in range(5):
            if not marks[board][i][j]:
                sum += boards[board][i][j]
    return sum


puzzle = Puzzle(year=2021, day=4)
data =  puzzle.input_data
drawn_numbers = [int(x) for x in data.split("\n\n")[0].split(",")]
boards = []
for board in range(1, len(data.split("\n\n"))):
    boards.append([[int(x.strip()) for x in y.split()] for y in data.split("\n\n")[board].split("\n")])
marks = [[[0 for i in range(5)] for j in range(5)] for k in range(len(boards))]

result_a = 0
for num in drawn_numbers:
    count = len(boards)
    mark_boards(boards, marks, num)
    winning_board = check_winning_boards(marks)
    if winning_board > -1 and not result_a:
        result_a = sum_board(boards, marks, winning_board) * num
    for i in range(len(boards)):
        count -= 1 * check_board(marks, i)
    if count == 1:
        losing_board = check_losing_boards(marks)
    elif count == 0:
        result_b = sum_board(boards, marks, losing_board) * num
        break


puzzle.answer_a = result_a
puzzle.answer_b = result_b
print(f"Part 1: {result_a}")
print(f"Part 2: {result_b}")
