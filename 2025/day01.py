with open("inputs/inp01.txt") as fh:
    lines = fh.read().strip().split('\n')

pos = 50
p1, p2 = 0, 0

for line in lines:
    dist = int(line[1:])
    to_zero = 0
    
    if line[0] == 'L':
        if pos == 0: to_zero = 100
        else: to_zero += pos
        pos -= dist

    if line[0] == 'R': 
        to_zero = 100 - pos
        pos += dist

    if dist >= to_zero:
        p2 += 1 + (dist - to_zero) // 100

    pos %= 100

    if pos == 0: p1 += 1

print("P1: ", p1)
print("P2: ", p2)