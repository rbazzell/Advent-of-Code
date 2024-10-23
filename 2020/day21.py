import sys, copy
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n")

class Recipe:
    def __init__(self, description: str):
        description = description.split(" (contains ")
        self.ingredients = description[0].split(" ")
        self.allergens = description[1][:-1].split(", ")

    def __repr__(self):
        return str(self.ingredients) + str(self.allergens)


recipes = [Recipe(line) for line in data]
possibilities = dict()
for recipe in recipes:
    for ingredient in recipe.ingredients:
        if not ingredient in possibilities.keys():
            possibilities[ingredient] = set()
        possibilities[ingredient].update(recipe.allergens)


def solution_a():
    global possibilities
    new_possibilities = copy.deepcopy(possibilities)
    for ingredient, allergens in possibilities.items():
        for allergen in allergens:
            for recipe in recipes:
                if allergen in recipe.allergens and not ingredient in recipe.ingredients and allergen in new_possibilities[ingredient]:
                    new_possibilities[ingredient].remove(allergen)
    
    possibilities = new_possibilities
    new_possibilities = copy.deepcopy(possibilities)
    sum = 0
    for ingredient, allergens in possibilities.items():
        for recipe in recipes:
            if len(allergens) == 0 and ingredient in recipe.ingredients:
                if ingredient in new_possibilities.keys():
                    new_possibilities.pop(ingredient)
                sum += 1
    possibilities = new_possibilities
    return sum


def solution_b():
    solution_a()
    for ingredient, allergens in possibilities.items():
        print(f"{ingredient}: {allergens}")

    

    for ingredient, allergens in possibilities.items():
        if len(allergens) == 1:
            break
    queue = [ingredient]

    allergens = {}
    while len(queue) > 0:
        ingredient = queue.pop()
        allergens[ingredient] = possibilities[ingredient].pop()
        possibilities.pop(ingredient)
        for i, a in possibilities.items():
            if ingredient in allergens.keys() and allergens[ingredient] in a:
                a.remove(allergens[ingredient])
            if len(a) == 1 and i not in queue:
                queue.append(i)
    
    canonical_dangerous_ingredients_list = ""
    allergens = {y: x for x, y in allergens.items()}
    sorted_allergens = list(allergens.keys())
    sorted_allergens.sort()
    for allergen in sorted_allergens:
        canonical_dangerous_ingredients_list += f"{allergens[allergen]},"

    return canonical_dangerous_ingredients_list[:-1]
        

        
        



#print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

