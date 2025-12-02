import time

startTime = time.time()
p1, p2 = 0, 0

with open("inputs/inp02.txt") as fh:
    lines = fh.read().strip().split(',')

for line in lines:
    first, last = line.split('-')
    for x in range(int(first), int(last)+1):
        x = str(x)
        if x[0:int(len(x)/2)] == x[int(len(x)/2):int(len(x))+1]:
            p1 += int(x)

        for y in range(2, len(x)+1):
            if len(x) % y == 0:
                test = list(map(''.join, zip(*[iter(x)]*int((len(x)/y)))))
                if test.count(test[0]) == y:
                    p2 += int(x)
                    break
    
print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))