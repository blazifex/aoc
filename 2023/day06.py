import time as clock, math

startTime = clock.time()

with open("inputs/inp06.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

times = list(map(int, INPUT[0].split(':')[1].split()))
recs = list(map(int, INPUT[1].split(':')[1].split()))
p1 = []

def check(time, rec):
    poss = 0
    for n in range(1,time): # don't check 0 secs or max secs as that will always be 0 movement
        dist = n * (time-n)
        if dist > rec: poss += 1
        elif poss > 0: break
    return poss

for id, time in enumerate(times):
    p1.append(check(time, recs[id]))

time2 = int(''.join(map(str, times)))
recs2 = int(''.join(map(str, recs)))
p2 = check(time2, recs2)

print(math.prod(p1))
print(p2)
print ('[Finished in {:.2f}ms]'.format(1000*(clock.time() - startTime)))