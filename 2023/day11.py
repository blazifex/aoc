from time import time
from itertools import combinations as combo

st_time = time()

gal, exp_r, exp_c = [], [], []

with open('inputs/inp11.txt') as fh:
    INPUT = [list(line) for line in fh.read().rstrip().split('\n')]

#check rows
for r, line in enumerate(INPUT): 
    if '#' not in line: exp_r.append(r)
    else:
        for c, char in enumerate(line):
            if char == '#': gal.append([r, c])
 
#check columns
for c in range(len(INPUT)):
    v = []
    for r, line in enumerate(INPUT):
        v.append(INPUT[r][c])
    if '#' not in v: exp_c.append(c)

def penalty(a, b, p):
    rows = [a[0], b[0]]
    cols = [a[1], b[1]]
    pen = 0
    for x in range(min(rows), max(rows)):
        if x in exp_r: pen += p
    for x in range(min(cols), max(cols)):
        if x in exp_c: pen += p
    return pen

def step(a, b, p):
    dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
    dist += penalty(a, b, p)
    return int(dist)

p1, p2 = [], []
for a, b in combo(gal, 2):
    p1.append(step(a, b, 1))
    p2.append(step(a, b, 999999))

print(sum(p1))
print(sum(p2))
print ('[Finished in {:.2f}ms]'.format(1000*(time() - st_time)))
