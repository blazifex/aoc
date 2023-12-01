import time, os, statistics

def main():
    with open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp07.txt","r") as f:
        input = [int(line) for line in f.read().split(',')]  
    input.sort()

    p1, p2 = 0, 0
    inp_median = int(statistics.median(input))
    inp_mean = int(sum(input)/len(input))

    for char in range(len(input)):
        p1+= abs(input[char] - inp_median)
        p2+= triNum(abs(input[char] - inp_mean))
    
    print("Part 1:", p1)
    print("Part 2:", p2)
    print(int(" 1   "))
def triNum(n): #http://en.wikipedia.org/wiki/Triangular_number
    return n * (n + 1) // 2

if __name__ == "__main__": 
    startTime = time.time()
    main()
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))