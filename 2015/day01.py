import time, math

start_time = time.time()
p1, p2 = 0, 0
p2_solved = False

with open("inputs/inp01.txt") as fh:
    input = fh.read().strip().split('\n')

for c, char in enumerate(input[0]):
    if char == '(': 
        p1 += 1
    elif char == ')': 
        p1 -= 1
    if p1 == -1 and not p2_solved: 
        p2 = c+1
        p2_solved = True

print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))