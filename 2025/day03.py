import time

start_time = time.time()
p1, p2 = 0, 0

with open("inputs/inp03.txt") as fh:
    input = fh.read().strip().split('\n')

def calc(n):
    total = 0
    for bank in input:
        batteries_needed = n
        complete = False
        left = 0
        active = ''

        while batteries_needed > 0 and not complete:
            right = len(bank) + 1 - batteries_needed
            bracket = bank[left:right]
            high_jolts = 0
            high_pos = 0

            for x in range(0, len(bracket)):
                current_jolts = int(bracket[x])
                if current_jolts > high_jolts:
                    high_jolts = current_jolts
                    high_pos = x

            active += str(high_jolts)
            left += high_pos + 1
            batteries_needed -= 1

            if batteries_needed == len(bank[left:]):
                active += bank[left:]
                complete = True

        total += int(active)

    return total

print("P1: ", calc(2))
print("P2: ", calc(12))
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))