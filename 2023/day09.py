from time import time

startTime = time()

with open("inputs/inp09.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

def get_next(nums):
    nxt = []
    for id, num in enumerate(nums[1:], 1):
        nxt.append(num - nums[id-1])
    if nxt.count(0) != len(nxt): nxt.append(nxt[-1] + get_next(nxt))
    else: nxt.append(0)
    return nxt[-1]

p1 = []
for line in INPUT:
    nums = list(map(int, line.split()))
    p1.append(nums[-1] + get_next(nums))

print(sum(p1))

def get_p2(nums):
    nxt = []
    for id, num in enumerate(nums[1:], 1):
        nxt.append(num - nums[id-1])
    if nxt.count(0) != len(nxt): nxt.append(nxt[0] - get_p2(nxt))
    else: nxt.append(0)
    return nxt[-1]

p2 = []
for line in INPUT:
    nums = list(map(int, line.split()))
    p2.append(nums[0] - get_p2(nums))

print(sum(p2))
print ('[Finished in {:.2f}ms]'.format(1000*(time() - startTime)))
