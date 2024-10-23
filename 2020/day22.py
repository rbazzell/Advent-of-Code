import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n\n")

player1 = [int(x) for x in data[0].split("\n")[1:]]
player2 = [int(x) for x in data[1].split("\n")[1:]]


def solution_a():
    p1 = player1.copy()
    p2 = player2.copy()

    while len(p1) > 0 and len(p2) > 0:
        card1 = p1.pop(0)
        card2 = p2.pop(0)

        if card1 > card2:
            p1.append(card1)
            p1.append(card2)
        
        if card2 > card1:
            p2.append(card2)
            p2.append(card1)

    winner = p1 if len(p1) > 0 else p2

    result = 0
    for i, c in enumerate(reversed(winner)):
        result += (i+1)*c
    return result

def solution_b():
    p1, p2, winner = recursive_combat(player1.copy(), player2.copy())
    winner = p1 if len(p1) > 0 else p2

    result = 0
    for i, c in enumerate(reversed(winner)):
        result += (i+1)*c
    return result


def recursive_combat(p1: list[int], p2:list[int]) -> tuple[list[int], list[int], bool]:
    if len(p1) == 0 or len(p2) == 0:
        return p1, p2, len(p1) > len(p2)
    

    previous_rounds = list()
    
    while len(p1) > 0 and len(p2) > 0:
        if (p1, p2) in previous_rounds:
            return p1, p2, True
        previous_rounds.append((p1.copy(),p2.copy()))
        card1 = p1.pop(0)
        card2 = p2.pop(0)

        if card1 <= len(p1) and card2 <= len(p2):
            winner = recursive_combat(p1.copy()[:card1], p2.copy()[:card2])[2]
            if winner:
                p1.append(card1)
                p1.append(card2)
            else:
                p2.append(card2)
                p2.append(card1)
        elif card1 > card2:
            winner = True
            p1.append(card1)
            p1.append(card2)
        elif card2 > card1:
            winner = False
            p2.append(card2)
            p2.append(card1)

    return p1, p2, winner


print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

