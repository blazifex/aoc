import time, os

def main():
    startTime = time.time()
    inp = [line.rstrip() for line in open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp03.txt","r").read().split('\n')]

    print("Part 1: ", p1(inp))
    print("Part 2: ", p2(inp, inp))
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))

def mostCommon(inp):
    tempList = []
    for n in inp:
        if inp[n].count('1') >= inp[n].count('0'): tempList.append('1')
        else: tempList.append('0')
    return tempList

def leastCommon(inp):
    tempList = []
    for n in inp:
        if inp[n].count('0') <= inp[n].count('1'): tempList.append('0')
        else: tempList.append('1')
    return tempList

def transposeVals(inp): #populate dictionary of values per column
    calcs = {}
    for x in range(len(inp)):
        for y in range (len(inp[x])):
            if calcs.get(y):
                calcs[y].append(inp[x][y])
            else: calcs[y] = [inp[x][y]]    
    return calcs

def listToStr(inp): #convert list to string
    x = ""
    for n in range(len(inp)):
        x += inp[n]
    return x

def refineList(list, keptIndex, pos): #keep items in a list that have indexes defined in a second list
    tempList = []
    for x in range(len(list)):
        if list[x][pos] == keptIndex[pos]:
            tempList.append(list[x])
    return tempList

def p1(inp):
    gamma = listToStr(mostCommon(transposeVals(inp)))
    epsilon = listToStr(leastCommon(transposeVals(inp)))
    return int(gamma, 2)*int(epsilon, 2)

def p2(o2gen, co2scrub):
    pos = 0 #calculate oxygen generator rating
    while len(o2gen) > 1:
        o2gen = refineList(o2gen, mostCommon(transposeVals(o2gen)), pos)      
        pos+=1

    pos=0 #calculate CO2 scrubber rating
    while len(co2scrub) > 1:
        co2scrub = refineList(co2scrub, leastCommon(transposeVals(co2scrub)), pos)  
        pos+=1

    return int(listToStr(o2gen[0]), 2) * int(listToStr(co2scrub[0]), 2)

if __name__ == "__main__": main()