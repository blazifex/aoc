import time

startTime = time.time()

with open("inputs/inp01.txt") as fh:
    blocks = fh.read().split('\n\n')
    blocks = [
        [int(food) for food in block.split('\n')]
        for block in blocks
    ]

cals = [sum(block) for block in blocks]
cals.sort()

print(f"p1: {max(cals)}")
print(f"p2: {sum(cals[-3:])}")

print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))