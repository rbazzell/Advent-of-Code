import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
from hashlib import md5

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

passcode = data
directions = "UDLR"

def solution_a():
    target = (3, 3)
    queue = [(0, 0, passcode)]
    while queue:
        x, y, code = queue.pop(0)

        if (x, y) == target:
            return code[len(passcode):]
        else:
            unlock = md5(code.encode()).hexdigest()[:4]
            open_dirs = [directions[i] for i, c in enumerate(unlock) if c in "bcdef"]
            for d in open_dirs:
                nx, ny = x, y
                match d:
                    case "D":
                        ny += 1
                    case "U":
                        ny -= 1
                    case "L":
                        nx -= 1
                    case "R":
                        nx += 1
                if 0 <= nx <= 3 and 0 <= ny <= 3:
                    queue.append((nx, ny, code + d))
    return None
            

def solution_b():
    target = (3, 3)
    longest_length = 0
    queue = [(0, 0, passcode)]
    while queue:
        x, y, code = queue.pop(0)

        if (x, y) == target:
            longest_length = max(len(code), longest_length)
        else:
            unlock = md5(code.encode()).hexdigest()[:4]
            open_dirs = [directions[i] for i, c in enumerate(unlock) if c in "bcdef"]
            for d in open_dirs:
                nx, ny = x, y
                match d:
                    case "D":
                        ny += 1
                    case "U":
                        ny -= 1
                    case "L":
                        nx -= 1
                    case "R":
                        nx += 1
                if 0 <= nx <= 3 and 0 <= ny <= 3:
                    queue.append((nx, ny, code + d))
    return longest_length - len(passcode)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

