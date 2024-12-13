import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
data = input_data

data = (line.split(" | ") for line in data.split("\n"))
data = ((signals.split(), values.split()) for signals, values in data)
data = tuple((tuple(frozenset(signal) for signal in line[0]), tuple(frozenset(value) for value in line[1])) for line in data)

def solution_a():
    ones_fours_sevens_eights = 0
    for signals, values in data:
        for value in values:
            if len(value) in (2, 4, 3, 7):
                ones_fours_sevens_eights += 1
    return ones_fours_sevens_eights

def solution_b():
    outputs = 0
    for signals, values in data:
        decypher = {}
        q = list(signals)
        while q:
            signal = q.pop(0)
            match len(signal):
                case 2:
                    decypher[signal] = 1
                    one = signal
                case 3:
                    decypher[signal] = 7
                case 4:
                    decypher[signal] = 4
                    four = signal
                case 5:
                    if 1 not in decypher.values() or 4 not in decypher.values():
                        q.append(signal)
                    else:
                        oneXOR = len(one ^ signal)
                        fourXOR = len(four ^ signal)
                        if oneXOR == fourXOR == 5:
                            decypher[signal] = 2
                        elif oneXOR == fourXOR == 3:
                            decypher[signal] = 3
                        else:
                            decypher[signal] = 5
                case 6:
                    if 1 not in decypher.values() or 4 not in decypher.values():
                        q.append(signal)
                    else:
                        oneXOR = len(one ^ signal)
                        fourXOR = len(four ^ signal)
                        if oneXOR == fourXOR:
                            decypher[signal] = 0
                        elif oneXOR == 6:
                            decypher[signal] = 6
                        else:
                            decypher[signal] = 9
                case 7:
                    decypher[signal] = 8

        code_str = ""
        for value in values:
            code_str += str(decypher[value])
        outputs += int(code_str)
    return outputs

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

