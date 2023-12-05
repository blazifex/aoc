import time

startTime = time.time()

with open("inputs/inp04.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

p1 = 0
p2 = [1] * len(INPUT)
vals = []
hand = list(range(1, len(INPUT)+1))

for line in INPUT:
    left, right = line.split(': ')[1].split('|')
    wins = len(set(left.split()) & set(right.split()))
    if wins > 0: p1 += 2**(wins-1)
    vals.append(wins)

for id, amt in enumerate(vals):
    for next in range(id + 1, id + amt + 1):
        p2[next] += p2[id]
    
print(p1) #part 1
print(sum(p2)) #part 2

print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))