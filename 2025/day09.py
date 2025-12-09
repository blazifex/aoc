import time

start_time = time.time()
p1, p2 = 0, 0

with open("inputs/inp09.txt") as fh:
    input = fh.read().strip().split('\n')

for r, row in enumerate(input):
    input[r] = [int(x) for x in row.split(',')]

areas = []
for r, row in enumerate(input):
    for x in range(r+1, len(input)):
        areas.append((max(row[0], input[x][0]) - min(row[0], input[x][0])+1) * (max(row[1], input[x][1]) - min(row[1], input[x][1])+1))

p1 = max(areas)

print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))