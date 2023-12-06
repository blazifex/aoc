import time

startTime = time.time()

with open("inputs/inp06.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

times = INPUT[0].split(':')[1].split()
recs = INPUT[0].split(':')[1].split()

for time in times:
    
    for n in range(1,int(time)): # don't check 0 secs or max secs as that will always be 0 movement
        print(n)