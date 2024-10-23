"""s1, l1 = 4, 4
s2, l2 = 0, 2
s3, l3 = 5, 2
s4, l4 = 3, 3
ranges = [s1, l1, s2, l2]"""

def overlap(s1, l1, s2, l2):
    e1 = s1 + l1 - 1
    e2 = s2 + l2 - 1
    s0 = max(s1, s2)
    l0 = min(e1, e2) - s0 + 1
    return s0, l0
"""
print(f"Same Range: {overlap(s1, l1, s1, l1)}")
print(f"No overlap (low end): {overlap(s1, l1, s2, l2)}")
print(f"No overlap (high end): {overlap(s2, l2, s1, l1)}")
print(f"Full range inside: {overlap(s1, l1, s3, l3)}")
print(f"Fully inside range: {overlap(s3, l3, s1, l1)}")
print(f"Partial overlap (s1 > s2): {overlap(s1, l1, s4, l4)}")
print(f"Partial overlap (s2 > s1): {overlap(s4, l4, s1, l1)}")
"""

def split_range(s, l, ss, sl):
    e = s + l - 1
    se = ss + sl - 1
    
    l1 = ss - s
    l2 = e - se

    return s, l1, ss, sl, se + 1, l2

#print(split_range(4, 4, 7, 1))

def conv_range(s1, l1, s2, l2):
    return s2, l1

"""os, ol = overlap(4, 4, 4, 2)
#print(conv_range(os, ol, 70, 2))

x, y = ranges.pop(0), ranges.pop(0)
print(x, y)"""


x = {0:1, 1:2, 2:3}
print(x[0])
print(x[4])