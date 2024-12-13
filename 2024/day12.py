import sys
sys.path.insert(0, '')
from misc import aoc_utilities as aocu
from collections import Counter

puzzle = aocu.get_puzzle(__file__)
examples = puzzle.examples #returns list of Example objects
input_data = puzzle.input_data #returns string of input data
    
data = examples[0].input_data
data = \
"""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
data = \
"""RRR.
RRRR
.R.R
.RR."""
data = input_data

farm = tuple(tuple(line) for line in data.split("\n"))

def adjacents(r, c):
    return {(r+1, c), (r-1, c), (r, c+1), (r, c-1)}

def solution_a():
    total_cost = 0
    visited = set()
    for fr, row in enumerate(farm):
        for fc, garden in enumerate(row):
            if (fr, fc) not in visited:
                area = 0
                q = [(fr, fc)]
                visited.add((fr, fc))
                edges = set()
                while q:                                                       
                    r, c = q.pop(0)
                    tr, tc = 2*r + 1, 2*c + 1
                    for er, ec in ((tr - 1, tc), (tr + 1, tc), (tr, tc-1), (tr, tc+1)):
                        if (er, ec) not in edges:
                            edges.add((er, ec))
                        else:
                            edges.discard((er, ec))
                    area += 1
                    for nr, nc in adjacents(r, c):
                        if 0 <= nr < len(farm) and 0 <= nc < len(farm[nr]) and farm[nr][nc] == garden and (nr, nc) not in visited:
                            q.append((nr, nc))
                            visited.add((nr, nc))
                perimeter = len(edges)
                total_cost += area * perimeter
    return total_cost

def solution_b():
    total_cost = 0
    visited = set()
    for fr, row in enumerate(farm):
        for fc, garden in enumerate(row):
            if (fr, fc) not in visited:
                area = 0
                q = [(fr, fc)]
                visited.add((fr, fc))
                edges = set()
                while q:                                                       
                    r, c = q.pop(0)
                    tr, tc = eton(r), eton(c)
                    for er, ec in ((tr - 1, tc), (tr + 1, tc), (tr, tc-1), (tr, tc+1)):
                        if (er, ec) not in edges:
                            edges.add((er, ec))
                        else:
                            edges.discard((er, ec))
                    area += 1
                    for nr, nc in adjacents(r, c):
                        if 0 <= nr < len(farm) and 0 <= nc < len(farm[nr]) and farm[nr][nc] == garden and (nr, nc) not in visited:
                            q.append((nr, nc))
                            visited.add((nr, nc))

                #count sides
                visited_edges = set()
                sides = 0
                for er, ec in edges:
                    if (er, ec) not in visited_edges:
                        q = [(er, ec)]
                        sides += 1
                        while q:
                            r, c = q.pop(0)
                            visited_edges.add((r,c))
                            vert = False
                            if r % 2 == 0:
                                nexts = ((r, c-2), (r, c+2))
                            elif c % 2 == 0:
                                nexts = ((r-2, c), (r+2, c))
                                vert = True

                            if vert:
                                left, right = (ntoe(r), ntoe(c-1)), (ntoe(r), ntoe(c+1))
                            else:
                                #really "down" and "up" here but whatever
                                left, right = (ntoe(r+1), ntoe(c)), (ntoe(r-1), ntoe(c))
                            for nr, nc in nexts:
                                if (nr, nc) in edges and (nr, nc) not in visited_edges:
                                    if vert:
                                        nleft, nright = (ntoe(nr), ntoe(nc-1)), (ntoe(nr), ntoe(nc+1))
                                    else:
                                        #really "down" and "up" here but whatever
                                        nleft, nright = (ntoe(nr+1), ntoe(nc)), (ntoe(nr-1), ntoe(nc))
                                    if (0 <= left[0] < len(farm) and 0 <= nleft[0] < len(farm) and 0 <= left[1] < len(farm[0])\
                                        and 0 <= nleft[1] < len(farm[0]) and farm[left[0]][left[1]] == farm[nleft[0]][nleft[1]]) \
                                        or (0 <= right[0] < len(farm) and 0 <= nright[0] < len(farm) and 0 <= right[1] < len(farm[0])\
                                        and 0 <= nright[1] < len(farm[0]) and farm[right[0]][right[1]] == farm[nright[0]][nright[1]]):
                                        q.append((nr, nc))
                total_cost += area * sides
    return total_cost

def ntoe(n: int) -> int:
    if n % 2 != 1:
        raise ValueError
    return (n - 1) // 2

def eton(e: int) -> int:
    return 2*e + 1

print(solution_b())
#puzzle.answer_a = solution_a()
#puzzle.answer_b = solution_b()

