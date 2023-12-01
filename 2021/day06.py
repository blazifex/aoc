import time, os

def main():
    with open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp06.txt","r") as inpFile:
        input = [line.rstrip() for line in inpFile.read().split(',')] 
    lanterns = []
    for line in range(len(input)):
        lanterns.append(int(input[line]))

    print("Part 1: ", birthing(lanterns, 80))
    print("Part 2: ", birthing(lanterns, 256))

def birthing(lanterns, days):
    calcs = dict((i, lanterns.count(i)) for i in lanterns)
    for _ in range(days):
        if 0 in calcs.keys(): 
            calcs["new"] = calcs.get(0)
            calcs["loop"] = calcs.pop(0)
        if 1 in calcs.keys(): calcs[0] = calcs.pop(1)
        if 2 in calcs.keys(): calcs[1] = calcs.pop(2)
        if 3 in calcs.keys(): calcs[2] = calcs.pop(3)
        if 4 in calcs.keys(): calcs[3] = calcs.pop(4)
        if 5 in calcs.keys(): calcs[4] = calcs.pop(5)
        if 6 in calcs.keys(): calcs[5] = calcs.pop(6)
        if 7 in calcs.keys(): calcs[6] = calcs.pop(7)
        if 8 in calcs.keys(): calcs[7] = calcs.pop(8)
        if "new" in calcs.keys(): calcs[8] = calcs.pop("new")
        if "loop" in calcs.keys(): 
            if 6 in calcs.keys(): calcs[6] = calcs.get(6)+calcs.pop("loop")
            else: calcs[6] = calcs.pop("loop")

    ans = 0
    for value in calcs.values():
        ans+= value
    return ans

if __name__ == "__main__": 
    startTime = time.time()
    main()
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))