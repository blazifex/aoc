from itertools import cycle as cy
import re
from functools import lru_cache
from math import lcm
from time import time

nodes = []

def main():
    startTime = time()
    with open("inputs/inp08.txt") as fh:
        INPUT = fh.read().rstrip()

    steps, block = INPUT.split('\n\n')
    a_locs = []

    for line in block.split('\n'):
        loc, l, r = re.findall(r'\w+', line)
        if loc[2] == 'A': a_locs.append(loc)
        nodes.append({'loc': loc, 'l': l, 'r': r})
    
    p1(steps)
    p2(steps, a_locs)
    print ('[Finished in {:.2f}ms]'.format(1000*(time() - startTime)))

@lru_cache
def get_next(step, loc):
    for node in nodes:
        if node['loc'] == loc:
            r = node['r']
            l = node['l']
    if step == 'R': loc = r
    else: loc = l
    return loc

def p1(steps):
    start = 'AAA'
    end = 'ZZZ'
    curr = start
    p1 = 0
    for step in cy(steps):
        if curr == end: break
        curr = get_next(step, curr)
        p1 += 1
    print(p1)

def p2(steps, a_locs):
    cyc_lens = []
    for loc in a_locs:
        cyc_len = 0
        curr = loc
        for step in cy(steps):
            curr = get_next(step, curr)
            cyc_len += 1
            if curr[2] == 'Z': break
        cyc_lens.append(cyc_len)
    print(lcm(*cyc_lens))

if __name__ == "__main__": main()