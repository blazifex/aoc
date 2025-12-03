import time

startTime = time.time()
p1, p2 = 0, 0

with open("inputs/inp03.txt") as fh:
    input = fh.read().strip().split('\n')

# Part 1
for bank in input:
    high = 0
    for x in range(len(bank)):
        for y in bank[x+1:]:
            test = int(bank[x] + y)
            if test > high:
                high = test
    p1 += high

# Part 2
for bank in input:
    complete = False
    batt_amt = 12
    left = 0

    while batt_amt > 0:
        if batt_amt == len(bank[left:]):
            active += bank[left:]
            complete = True
        if not complete:
            max_jolts = 0
            right = left+len(bank)-batt_amt
            active = ''
            bracket = bank[left:right+1]
            for x in range(len(bracket)):
                curr_jolts = int(bracket[x])
                if curr_jolts > max_jolts:
                    max_jolts = curr_jolts
                    max_pos = x
            active += str(max_jolts)
            left += max_pos+1
            batt_amt -= 1

    p2+=int(active)
    
# Outputs
print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))