from time import time

startTime = time()
p1, p2 = [], []

with open("inputs/inp09.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

def get_next(l, rev): # reversed math for p2
    nxt = []
    for id, n in enumerate(l[1:], 1): nxt.append(n - l[id-1])    
    if nxt.count(0) == len(nxt): return 0
    if rev: return nxt[0] - get_next(nxt, 1) 
    else: return nxt[-1] + get_next(nxt, 0)

for line in INPUT:
    x = list(map(int, line.split()))
    p1.append(x[-1] + get_next(x, 0))
    p2.append(x[0] - get_next(x, 1))

print(sum(p1))
print(sum(p2))
print ('[Finished in {:.2f}ms]'.format(1000*(time() - startTime)))