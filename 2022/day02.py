import time

startTime = time.time()

with open("inputs/inp02.txt") as fh:
    blocks = fh.read().split('\n')

values = {'X': 1, 'Y': 2, 'Z': 3}
wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
ties = {'A': 'X', 'B': 'Y', 'C': 'Z'}
losses = {'A': 'Z', 'B': 'X', 'C': 'Y'}
p1, p2 = 0, 0

for block in blocks:
    p1+=values[block[-1]]
    if block[-1] == wins[block[0]]: p1+= 6
    elif block[-1] == ties[block[0]]: p1+= 3

for block in blocks:
    if block[-1] == 'X':
        p2+=values[losses[block[0]]]
    elif block[-1] == 'Y':
        p2+=values[ties[block[0]]]
        p2+=3 #score for tie
    elif block[-1] == 'Z':
        p2+=values[wins[block[0]]]
        p2+=6 #score for win

print(f"p1: {p1}")
print(f"p2: {p2}")

print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))