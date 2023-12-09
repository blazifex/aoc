from time import time

startTime = time()
p1, p2 = [], []

with open("inputs/inp09.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

def get_next(nums, part):
    nxt = []
    for id, num in enumerate(nums[1:], 1):
        nxt.append(num - nums[id-1])
    if nxt.count(0) != len(nxt): 
        if part == 1: nxt.append(nxt[-1] + get_next(nxt, 1))
        else: nxt.append(nxt[0] - get_next(nxt, 2))
    else: nxt.append(0)
    return nxt[-1]

for line in INPUT:
    nums = list(map(int, line.split()))
    p1.append(nums[-1] + get_next(nums, 1))
    p2.append(nums[0] - get_next(nums, 2))

print(sum(p1))
print(sum(p2))
print ('[Finished in {:.2f}ms]'.format(1000*(time() - startTime)))