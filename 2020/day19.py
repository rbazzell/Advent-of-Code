import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(19, 2020)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[1].input_data
data = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""


data = input_data

data = data.split("\n\n")

#list/dictionary comprehension is WILD
#since this in unreadable, let me explain
#     example:                 0 : [[1, 2], [2, 3]]    is    0: 1 2 | 2 3
#          the rule id (int)     : list of lists of rules in their order 
grammar = {int(x.split(": ")[0]) : [[int(z) if z.isnumeric() else z.strip("\"") for z in y.split(" ")] for y in x.split(": ")[1].split(" | ")] for x in data[0].split("\n")}
messages = data[1].split("\n")

def match(start: int, message: str, i: int):
    if i >= len(message):
        return i, False
    rules = grammar[start]

    #rules contains the right side of the specific rule
    #rule  cotnains each specific part of the or 
    #sub_rule contains each specific int
    starti = i
    overvalid = False
    for rule in rules:
        j = starti
        valid = True  
        for sub_rule in rule:
            if sub_rule == 8 and len(grammar[8]) > 1:
                available = True
                count42 = 0
                while available:
                    available = False
                    for f in fit(42):
                        if j + len(f) > len(message):
                            break
                        if message[j:j+len(f)] == f:
                            count42 += 1
                            j = j + len(f)
                            available = True
                            break
                valid = count42 > 0
            elif sub_rule == 11 and len(grammar[11]) > 1:
                old_42s = 0
                k = j
                dec = len(fit(42)[0])
                while k - dec >= 0 and message[k-dec:k] in fit(42):#ungrabs the most recent one, just in case previous was 8
                    k -= dec
                    old_42s += 1
                available = True
                count42 = 0
                while available:
                    available = False
                    for f in fit(42):
                        if j + len(f) > len(message):
                            break
                        if message[j:j+len(f)] == f:
                            count42 += 1
                            j = j + len(f)
                            available = True
                            break
                if not valid:
                    break
                available = True
                count31 = 0
                while available:
                    available = False
                    for f in fit(31):
                        if j + len(f) > len(message):
                            break
                        if message[j:j+len(f)] == f:
                            count31 += 1
                            j = j + len(f)
                            available = True
                            break
                valid = count42 + old_42s >= count31 and count31 > 0
            elif isinstance(sub_rule, int):
                j, check = match(sub_rule, message, j)
                valid = valid and check
            else: #"a" or "b"
                return i + 1, message[i] == sub_rule
        if valid and j > i:
            i = j
            overvalid = True
    return i, overvalid


def firsts(start: int):
    rules = grammar[start]
    fs = list()

    for rule in rules:
        if rule[0] not in fs:
            fs.append(rule[0])
    return fs


def fit(start: int):
    rules = grammar[start]

    fits = []
    
    for rule in rules:
        skip = False
        underfits = [""]
        
        for sub_rule in rule: 
            if sub_rule == start:
                skip = True
                break
            if isinstance(sub_rule, int):
                f = fit(sub_rule)
                newfits = ["" for i in range(len(f) * len(underfits))]
                for i in range(len(f)):
                    for u in range(len(underfits)):
                        newfits[i * len(underfits) + u] = underfits[u] + f[i] ## the i + 2u indexing is wrong
                underfits = newfits
            else:
                return sub_rule
        if skip:
            continue
        fits.extend(underfits)
    return fits


def solution_a():
    sum = 0
    for message in messages:
        i, check = match(0, message, 0)
        if check and i == len(message):
            sum += 1
    return sum


def solution_b():
    #update grammar:
    grammar[8] = [[42], [42, 8]]
    grammar[11] = [[42, 31], [42, 11, 31]]
    
    #solution with updated grammar:
    sum = 0
    for j, message in enumerate(messages):
        check = False
        i = 0
        i, check = match(0, message, 0)
        if check and i == len(message):
            sum += 1
        #print(f"{j+1}.) {check and i == len(message)} - {message}")

    #revert grammar:
    grammar[8] = [[42]]
    grammar[11] = [[42, 31]]

    #return
    return sum


print(solution_b())
#puzzle.answer_a = solution_a()
puzzle.answer_b = solution_b()

