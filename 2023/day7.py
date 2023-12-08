from aocd.models import Puzzle
import os
import functools
os.environ["AOC_SESSION"] = "53616c7465645f5f8bff693a28ddc555a8233386bd6b1ad7e554d5c83830f2ea1712910385002a2567dd54ec3ae2321a7cb563c5dda138661eb4b1697bc4f472" # handout: exclude

CARD_VALUES = { 
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 1, # j= 11 if no joker, j=1 if joker
    "T" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
    }

HAND_VALUES = {
    (5, 0) : 6, #five of a kind
    (4, 1) : 5, #four of a kind
    (3, 2) : 4, #full house
    (3, 1) : 3, #three of a kind
    (2, 2) : 2, #two pair
    (2, 1) : 1, #one pair
    (1, 1) : 0, #high card
}


def parse_input(data):
    data = data.split("\n")
    return [y.split(" ")[0] for y in data], [int(x) for x in [y.split()[1]for y in data]]


def comp_hands_no_joker(h1, h2):
    t1 = [0 for i in range(13)]
    t2 = [0 for i in range(13)]
    for c1, c2 in zip(h1, h2):
        t1[CARD_VALUES[c1] - 2] += 1
        t2[CARD_VALUES[c2] - 2] += 1
    t1.sort(reverse=True)
    t2.sort(reverse=True)
    if HAND_VALUES[(t1[0], t1[1])] > HAND_VALUES[(t2[0], t2[1])]:
        return 1
    elif HAND_VALUES[(t2[0], t2[1])] > HAND_VALUES[(t1[0], t1[1])]:
        return -1
    else:
        for c1, c2 in zip(h1, h2):
            if CARD_VALUES[c1] > CARD_VALUES[c2]:
                return 1
            if CARD_VALUES[c2] > CARD_VALUES[c1]:
                return -1
    return 0

def comp_hands_joker(h1, h2):
    t1 = [0 for i in range(14)]
    t2 = [0 for i in range(14)]
    for c1, c2 in zip(h1, h2):
        t1[CARD_VALUES[c1] - 2] += 1
        t2[CARD_VALUES[c2] - 2] += 1
    t1, w1 = t1[:-1], t1[-1]
    t2, w2 = t2[:-1], t2[-1]
    t1.sort(reverse=True)
    t2.sort(reverse=True)
    t1[0] += w1
    t2[0] += w2
    if HAND_VALUES[(t1[0], t1[1])] > HAND_VALUES[(t2[0], t2[1])]:
        return 1
    elif HAND_VALUES[(t2[0], t2[1])] > HAND_VALUES[(t1[0], t1[1])]:
        return -1
    else:
        for c1, c2 in zip(h1, h2):
            if CARD_VALUES[c1] > CARD_VALUES[c2]:
                return 1
            if CARD_VALUES[c2] > CARD_VALUES[c1]:
                return -1
    return 0

puzzle = Puzzle(year=2023, day=7)
data = puzzle.examples[0].input_data
data = puzzle.input_data
hands, bets = parse_input(data)
game = {hand : bet for hand, bet in zip(hands, bets)}

game_a = sorted(game.keys(), key=functools.cmp_to_key(comp_hands_no_joker))
game_b = sorted(game.keys(), key=functools.cmp_to_key(comp_hands_joker))


ans_a = 0
ans_b = 0

for i, hand in enumerate(game_a):
    ans_a += (i + 1) * game[hand]

for i, hand in enumerate(game_b):
    ans_b += (i + 1) * game[hand]
    print(i + 1, hand, "*", game[hand], "=", (i + 1) * game[hand])


print(f"Answer 1: {ans_a}")
print(f"Answer 2: {ans_b}")


#puzzle.answer_a = ans_a
puzzle.answer_b = ans_b