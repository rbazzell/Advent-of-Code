import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = examples[0].input_data
data = input_data

data = data.split("\n\n")

start = data[0].split("\n")
start_state = start[0].split(" ")[-1][:-1]
steps = int(start[1].split(" ")[-2])

states = {}
for section in data[1:]:
    section = section.split("\n")
    state = section[0].split(" ")[-1][:-1]
    
    #for 0s:
    zero_write = int(section[2].split(" ")[-1][:-1])
    zero_dir = 1 if section[3].split(" ")[-1] == "right." else -1
    zero_next_state = section[4].split(" ")[-1][:-1]
    
    #for 1s:
    one_write = int(section[6].split(" ")[-1][:-1])
    one_dir = 1 if section[7].split(" ")[-1] == "right." else -1
    one_next_state = section[8].split(" ")[-1][:-1]

    states[state] = ((zero_write, zero_dir, zero_next_state), \
                    (one_write, one_dir, one_next_state))
def solution_a():
    state = start_state
    tape = {0: 0}
    curr = 0
    for _ in range(steps):
        if curr not in tape:
            tape[curr] = 0
        write, dir, next_state = states[state][tape[curr]]
        tape[curr] = write
        curr += dir
        state = next_state
    return sum(tape.values())

        

def solution_b():
    pass

print(solution_a())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

