import time

startTime = time.time()
p1, p2 = 0, 0

with open("inputs/inp03.txt") as fh:
    input = fh.read().strip().split('\n')

def calc(val):
    ans = 0
    for bank in input:
        batt_amt = val
        complete = False
        left = 0
        active = ''

        while batt_amt > 0:
            if batt_amt == len(bank[left:]):
                active += bank[left:]
                complete = True
            if not complete:
                right = len(bank)-batt_amt
                bracket = bank[left:right+1]
                max_jolts = 0
                max_pos = 0
                for x in range(0, len(bracket)):
                    curr_jolts = int(bracket[x])
                    if curr_jolts > max_jolts:
                        max_jolts = curr_jolts
                        max_pos = x
                active += str(max_jolts)
                left += max_pos+1
            batt_amt -= 1
        ans += int(active)
    return ans

print("P1: ", calc(2))
print("P2: ", calc(12))

print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))