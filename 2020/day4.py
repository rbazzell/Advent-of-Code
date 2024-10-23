import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
import copy

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

#data = examples[0].input_data
data = input_data

data = data.split("\n\n")
data = [x.split() for x in data]

base_passport = {"byr" : None,
                 "iyr" : None, 
                 "eyr" : None, 
                 "hgt" : None, 
                 "hcl" : None, 
                 "ecl" : None, 
                 "pid" : None, 
                 "cid" : None}

passports = list()
for datum in data:
    passport = copy.deepcopy(base_passport)
    for line in datum:
        passport[line[0:3]] = line[4:]
    passports.append(passport)

def solution_a():
    valid_passports = 0
    for passport in passports:
        valid = True
        for key, value in passport.items():
            if key != "cid" and value == None:
                valid = False
                break
        if valid:
            valid_passports += 1
    return valid_passports


            
def solution_b():
    valid_passports = 0
    for passport in passports:
        valid = True
        for key, value in passport.items():
            if key != "cid" and value == None:
                valid = False
                break
            match key:
                case "byr":
                    value = int(value)
                    if value < 1920 or value > 2002:
                        valid = False
                        break
                case "iyr":
                    value = int(value)
                    if value < 2010 or value > 2020:
                        valid = False
                        break
                case "eyr":
                    value = int(value)
                    if value < 2020 or value > 2030:
                        valid = False
                        break
                case "hgt":
                    cm = value[-2:] == "cm"
                    value = int(value[:-2])
                    if cm and (value < 150 or value > 193):
                        valid = False
                        break
                    if not cm and (value < 59 or value > 76):
                        valid = False
                        break
                case "hcl":
                    value = value[1:]
                    if set(value) in set("0123456789abcdef") or not len(value) == 6:
                        valid = False
                        break
                case "ecl":
                    if value not in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                        valid = False
                        break
                case "pid":
                    if len(value) != 9 or not value.isnumeric():
                        valid = False
                        break
                case "cid":
                    continue
        if valid:
            valid_passports += 1
    return valid_passports


print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

