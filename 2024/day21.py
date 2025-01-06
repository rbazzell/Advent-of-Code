import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data

data = \
"""029A
980A
179A
456A
379A"""
data = input_data

data = data.split("\n")

def solution_a():
    return compute_score(3)

def compute_score(panels):
    #definitely a way to find this using bfs, dfs, or dijkstra's -> faster for me to find it and code it manually
    #when more than 1 path was an option, I worked out on paper which way was faster. Here are the rules I found:
    # 1.) always keep directions together (i.e.  "<<^^" is ALWAYS faster than "<^<^" or "<^^<", since the next robot doesn't have to move)
    #     This gives us only 1 or 2 options per path (i.e.  "<<^^" or "^^<<", or if just "^", we only have 1)
    # 2.) If either of these 2 options has us traveling through the invalid spot on the keypad, use the other
    # 3.) Otherwise, the priority order goes "<^v>". ("^v" are actually at the same priority, but this never causes problems since "^v" is just "")
    #     This can be seen by writing it out - take the two paths: "         <      ^   A" and "       ^        <       A". 
    #     One level up, they still are the same length:            "  v <<   A >  ^ A > A" and "   <   A  v <   A >>  ^ A".
    #     Two levels up, and the problem appears:                  "<vA<AA>>^AvA<^A>AvA^A" and "v<<A>>^A<vA<A>>^AvAA<^A>A".
    #                                                                      len = 21                   len = 25
    #     Essentially, it makes the robot one level up cover more things along its path of movement, which makes the robot two levels up more efficient

    num_paths: dict[str, dict[str, list[str]]] = {
        'A': {'A':"",      '0':"<",    '1':"^<<",  '2':"<^",  '3':"^",    '4':"^^<<", '5':"<^^", '6':"^^",  '7':"^^^<<", '8':"<^^^", '9':"^^^"},
        '0': {'A':">",     '0':"",     '1':"^<",   '2':"^",   '3':"^>",   '4':"^^<",  '5':"^^",  '6':"^^>", '7':"^^^<",  '8':"^^^",  '9':"^^^>"},
        '1': {'A':">>v",   '0':">v",   '1':"",     '2':">",   '3':">>",   '4':"^",    '5':"^>",  '6':"^>>", '7':"^^",    '8':"^^>",  '9':"^^>>"},
        '2': {'A':"v>",    '0':"v",    '1':"<",    '2':"",    '3':">",    '4':"<^",   '5':"^",   '6':"^>",  '7':"<^^",   '8':"^^",   '9':"^^>"},
        '3': {'A':"v",     '0':"<v",   '1':"<<",   '2':"<",   '3':"",     '4':"<<^",  '5':"<^",  '6':"^",   '7':"<<^^",  '8':"<^^",  '9':"^^"},
        '4': {'A':">>vv",  '0':">vv",  '1':"v",    '2':"v>",  '3':"v>>",  '4':"",     '5':">",   '6':">>",  '7':"^",     '8':"^>",   '9':"^>>"},
        '5': {'A':"vv>",   '0':"vv",   '1':"<v",   '2':"v",   '3':"v>",   '4':"<",    '5':"",    '6':">",   '7':"<^",    '8':"^",    '9':"^>"},
        '6': {'A':"vv",    '0':"<vv",  '1':"<<v",  '2':"<v",  '3':"v",    '4':"<<",   '5':"<",   '6':"",    '7':"<<^",   '8':"<^",   '9':"^"},
        '7': {'A':">>vvv", '0':">vvv", '1':"vv",   '2':"vv>", '3':"vv>>", '4':"v",    '5':"v>",  '6':"v>>", '7':"",      '8':">",    '9':">>"},
        '8': {'A':"vvv>",  '0':"vvv",  '1':"<vv",  '2':"vv",  '3':"vv>",  '4':"<v",   '5':"v",   '6':"v>",  '7':"<",     '8':"",     '9':">"},
        '9': {'A':"vvv",   '0':"<vvv", '1':"<<vv", '2':"<vv", '3':"vv",   '4':"<<v",  '5':"<v",  '6':"v",   '7':"<<",    '8':"<",    '9':""}
    }
    arrow_paths: dict[str, dict[str, list[str]]] = {
        '<':{'<':"",    'v': ">",  '>':">>", '^':">^", 'A':">>^"},
        'v':{'<':"<",   'v': "",   '>':">",  '^':"^",  'A':"^>"},
        '>':{'<':"<<",  'v': "<",  '>':"",   '^':"<^", 'A':"^"},
        '^':{'<':"v<",  'v': "v",  '>':"v>", '^':"",   'A':">"},
        'A':{'<':"v<<", 'v': "<v", '>':"v",  '^':"<",  'A':""}
    }

    score = 0
    for line in data:
        path = control_robot({line: 1}, num_paths)
        for _ in range(panels - 1):
            path = control_robot(path, arrow_paths)
        score += sum(len(p) * v for p, v in path.items()) * int(line[:-1])
    return score

def control_robot(sequence: dict[str, int], paths: dict[str, dict[str, str]]) -> dict[str, int]:
    # Dynamic Programming! (Some guy on reddit called this style of DP "glowfishing", which I really like - named after day8year2021's glowfish problem)
    # Essentially, group like sub structures, to reduce computation. If we have a pattern that is "363A", one level up, the path is "^A^AvAvA".
    # To prevent us from calculation the path from A to ^ to A twice and the path from A to v to A twice, we can store the path as a dictionary like
    # {"^A" : 2, "vA" : 2}, perform the calculation for each "subpath" one time, and then add 2 to the result's value in a result dictionary
    # Doesn't save much time in this example, but saves an astronomical amount of time in much larger cases
    path: dict[str, int] = dict()
    for subseq, v in sequence.items():
        prev = 'A'
        for s in subseq:
            ss = paths[prev][s] + 'A'
            if ss not in path:
                path[ss] = 0
            path[ss] += v
            prev = s
    return path

def solution_b():
    return compute_score(26)

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()


