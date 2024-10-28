import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

#data = examples[0].input_data
data = """Hit Points: 13
Damage: 8"""
data = input_data

data = data.split("\n")
BOSS = (int(data[0].split(" ")[-1]), int(data[1].split(" ")[-1]))
SPELLS = {"magic missile":53, "drain": 73, "shield": 113, "poison": 173, "recharge": 229}

def battle(hard_mode:bool=False):
    boss_health = BOSS[0]
    player_health = 50
    player_mana = 500
    return min([battler(player_health, player_mana, boss_health, True, (0,0,0), spell, hard_mode) for spell in SPELLS.keys()])

def battler(p_hp: int, mana:int, b_hp: int, p_turn:bool, turns_left:tuple[int,int,int], spell:str, hard_mode:bool):
    if mana < 0:
        return 2147483647
    if hard_mode and p_turn:
        p_hp -= 1
        if p_hp <= 0:
            return 2147483647
    boss_damage = BOSS[1]

    shield_turns_left = turns_left[0]
    poison_turns_left = turns_left[1]
    recharge_turns_left = turns_left[2]

    if shield_turns_left:
        shield_turns_left -= 1
        player_armor = 7
    else:
        player_armor = 0
    if poison_turns_left:
        poison_turns_left -= 1
        b_hp -= 3
        if b_hp <= 0:
            return 0
    if recharge_turns_left:
        recharge_turns_left -= 1
        mana += 101

    

    if p_turn:
        match spell:
            case "magic missile":
                b_hp -= 4
            case "drain":
                b_hp -= 2
                p_hp += 2
            case "shield":
                if shield_turns_left:
                    return 2147483647
                shield_turns_left = 6
            case "poison":
                if poison_turns_left:
                    return 2147483647
                poison_turns_left = 6
            case "recharge":
                if recharge_turns_left:
                    return 2147483647
                recharge_turns_left = 5
        
        if b_hp <= 0:
            return SPELLS[spell]
        else:
            turns_left = (shield_turns_left, poison_turns_left, recharge_turns_left)
            return SPELLS[spell] + min([battler(p_hp, mana - SPELLS[spell], b_hp, False, turns_left, s, hard_mode) for s in SPELLS.keys()])

    else:
        p_hp -= max(1, boss_damage - player_armor)
        if p_hp <= 0:
            return 2147483647
        else:
            turns_left = (shield_turns_left, poison_turns_left, recharge_turns_left)
            return battler(p_hp, mana, b_hp, True, turns_left, spell, hard_mode)
        


def solution_a():
    return battle()

def solution_b():
    return battle(hard_mode=True)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

