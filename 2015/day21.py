import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

#data = examples[0].input_data
data = input_data

data = data.split("\n")

BOSS = (int(data[0].split(" ")[-1]), int(data[1].split(" ")[-1]), int(data[2].split(" ")[-1]))

weapon_shop = {8:4,
               10:5,
               25:6,
               40:7,
               74:8}
armor_shop = {0:0,
              13:1,
              31:2,
              53:3,
              75:4,
              102:5}

ring_shop = {0: (0, 0),
             25: (1, 0),
             50: (2, 0),
             100: (3, 0),
             20: (0, 1),
             40: (0, 2),
             80: (0, 3)}

def battle(player_damage: int, player_armor: int) -> bool:
    '''Simulates a battle: returns True if player wins'''
    boss_health: int = BOSS[0]
    boss_damage: int = BOSS[1]
    boss_armor: int = BOSS[2]
    player_health: int = 100
    p_turn = True
    while player_health > 0 and boss_health > 0:
        if p_turn:
            boss_health -= max(1, player_damage - boss_armor)
        else:
            player_health -= max(1, boss_damage - player_armor)
        p_turn = not p_turn
                #player wins after their turn   OR  #boss wins after their turn
    return (not p_turn and boss_health <= 0) or not (p_turn or player_health <= 0) #boss would die first
    


def solution_a():
    min_gold = 99999999
    for wg, weapon in weapon_shop.items():
        for ag, armor in armor_shop.items():
            for r1g, ring1 in ring_shop.items():
                for r2g, ring2 in ring_shop.items():
                    if len(set([r1g, r2g])) < 2 - [r1g, r2g].count(0):
                        continue
                    rings = tuple(ring1[i] + ring2[i] for i in range(2))
                    if battle(weapon + rings[0], armor + rings[1]):
                        min_gold = min(min_gold, wg + ag + r1g + r2g)
    return min_gold

def solution_b():
    max_gold = -1
    for wg, weapon in reversed(weapon_shop.items()):
        for ag, armor in reversed(armor_shop.items()):
            for r1g, ring1 in reversed(ring_shop.items()):
                for r2g, ring2 in reversed(ring_shop.items()):
                    if len(set([r1g, r2g])) < 2 - [r1g, r2g].count(0):
                        continue
                    rings = tuple(ring1[i] + ring2[i] for i in range(2))
                    if not battle(weapon + rings[0], armor + rings[1]):
                        max_gold = max(max_gold, wg + ag + r1g + r2g)
    return max_gold

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

