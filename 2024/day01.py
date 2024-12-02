with open("inp01.txt") as fh:
    lines = fh.read().split('\n')

l, r = [], []
p1, p2 = 0, 0

for line in lines:
    line = line.split()
    l.append(int(line[0]))
    r.append(int(line[-1]))

l.sort()
r.sort()

for n in range(len(l)):
    p1+= max(r[n],l[n]) - min(r[n],l[n])
    p2+= l[n] * r.count(l[n])

print('P1: ', p1)
print('P2: ', p2)