import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[7].input_data
data = "[1,{\"c\":\"red\",\"b\":2},3]"
data = input_data

data: list[str] = data.split("\n")


def solution_a():
    sum = 0
    for line in data:
        i = 0
        while i < len(line):
            num = ""
            j = i
            while line[i].isdigit():
                num += line[i]
                i += 1
            num = 0 if not num else int(num)
            if line[j-1] == '-':
                sum -= num
            else:
                sum += num
            i += 1
    return sum
            


                
def sum_object(i:int, line:str, red:bool):
    sum = 0
    while line[i] != '}':
        if line[i] == '{':
            i, s = sum_object(i + 1, line, red)
            sum += s
        elif not red and line[i:i+5] == ":\"red":
            i += 5
            red = True
        elif not red and line[i].isdigit():
            num = ""
            j = i
            while line[i].isdigit():
                num += line[i]
                i += 1
            num = 0 if not num else int(num)
            if line[j-1] == '-':
                sum -= num
            else:
                sum += num
        else:
            i += 1
    
    return i + 1, (0 if red else sum)

def solution_b():
    sum = 0
    for line in data:
        i = 0
        while i < len(line):
            if line[i] == '{':
                i, s = sum_object(i + 1, line, False)
                sum += s
            elif line[i].isdigit():
                num = ""
                j = i
                while line[i].isdigit():
                    num += line[i]
                    i += 1
                num = 0 if not num else int(num)
                if line[j-1] == '-':
                    sum -= num
                else:
                    sum += num
            else:
                i += 1
    return sum

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

