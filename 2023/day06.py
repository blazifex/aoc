import time as clock, math

startTime = clock.time()

with open("inputs/inp06.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

times = list(map(int, INPUT[0].split(':')[1].split()))
recs = list(map(int, INPUT[1].split(':')[1].split()))
p1 = []

"""def check(time, rec):
    poss = 0
    for held in range(1,time): # don't check 0 secs or max secs as that will always be 0 movement
        dist = held * (time-held)
        if dist > rec: poss += 1
        elif poss > 0: break
    return poss"""

'''
if d = h * (t-h)

d = ht - h^2, or

-h^2 + ht - d = 0

quadratic equation:

ax^2 + bx + c = 0, so

a = -1
x = h
b = t
c = -d

quadratic equation soln:

x = (-b +/- sqrt(b^2 - 4ac))/2a

therefore:

h = (-t + sqrt(t**2 - 4 * ((-1) * -d)))/(2*-1)
'''

def check(t, d):
    d+=1 # we want our solution to be at least 1 more unit than the req. distance
    h1 = math.floor((-t - math.sqrt(t**2 - 4 * ((-1) * -d)))/(2*(-1)))
    h2 = math.ceil((-t + math.sqrt(t**2 - 4 * ((-1) * -d)))/(2*(-1)))
    return abs(h2 - h1) + 1

for id, time in enumerate(times):
    p1.append(check(time, recs[id]))

t = int(''.join(map(str, times)))
d = int(''.join(map(str, recs))) 

p2 = check(t,d)

print(math.prod(p1))
print(p2)
print ('[Finished in {:.2f}ms]'.format(1000*(clock.time() - startTime)))