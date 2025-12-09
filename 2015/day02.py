import time, math

start_time = time.time()
p1, p2 = 0, 0

with open("inputs/inp02.txt") as fh:
    input = fh.read().strip().split('\n')

for line in input:
    l, w, h = map(int,line.split('x'))
    sides = []
    sides.append(2*l*w)
    sides.append(2*w*h)
    sides.append(2*h*l)
    p1 += int(sum(sides)+(min(sides)/2))
    dimensions = sorted([l,w,h])
    p2 += (dimensions[0] * 2) + (dimensions[1] * 2) + (l*w*h)



print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))