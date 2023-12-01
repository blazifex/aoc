import time, os

startTime = time.time()
inp = [int(line.rstrip()) for line in open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp01.txt","r").read().split('\n')]

print("Part 1: ", sum(x < y for x, y in zip(inp, inp[1:])))
print("Part 2: ", sum(x < y for x, y in zip(inp, inp[3:])))
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))

""" def main():
    startTime = time.time()
    inp = [int(line.rstrip()) for line in open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp01.txt","r").read().split('\n')]

    print("Part 1: ", p1(inp, 0))
    print("Part 2: ", p2(inp, 0))
    print ('[Finished in {:.5f}s]'.format(time.time() - startTime))

def p1(inp, ans):
    for n in range(1, len(inp)):
        if inp[n] > inp[n-1]: ans+=1
    return ans

def p2(inp, ans):
    for n in range(1, len(inp)-2):
        if inp[n+2] > inp[n-1]: ans+=1 #inp[n] and inp[n+1] are in both comparisons so can be excluded from calculation
    return ans

if __name__ == "__main__": main() """