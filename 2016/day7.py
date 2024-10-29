import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = "aaa[kek]eke"
data = input_data

data = data.split("\n")


def is_abba(s:str):
    return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]

def is_aba(s:str):
    return s[0] == s[2] and s[0] != s[1]

def get_bab(s:str):
    return s[1] + s[0] + s[1]


def solution_a():
    tls_count = 0
    for ip in data:
        supports_tls = False
        in_brackets = False
        for i in range(len(ip) - 3):
            if ip[i] in "[]":
                in_brackets = not in_brackets
                continue
            s = ip[i:i+4]
            if is_abba(s) and not in_brackets:
                supports_tls = True
            elif is_abba(s) and in_brackets:
                supports_tls = False
                break
        if supports_tls:
            tls_count += 1
    return tls_count

                


def solution_b():
    tls_count = 0
    for ip in data:
        in_brackets = False
        abas = []
        babs = []
        for i in range(len(ip) - 2):
            if ip[i] in "[]":
                in_brackets = not in_brackets
                continue
            s = ip[i:i+3]
            if is_aba(s) and in_brackets:
                if get_bab(s) in babs:
                    tls_count += 1
                    break
                abas.append(s)
            elif is_aba(s) and not in_brackets:
                babs.append(s)
                if get_bab(s) in abas:
                    tls_count += 1
                    break
            
    return tls_count

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

