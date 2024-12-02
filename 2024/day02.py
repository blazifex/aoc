import copy
with open("inp02.txt") as fh: 
    lines = fh.read().strip().split('\n')

p1, p2 = 0, 0

def checkSafe(line: list):
    for x in range(len(line)-1):
        if not 1 <= (abs(int(line[x]) - int(line[x+1]))) <= 3: return False
    return True

def solve(line: list, ans = 0):
    if line == sorted(line) or line == sorted(line, reverse=True):
        if checkSafe(line): return True
    return False

for line in lines:
    line = [int(x) for x in line.split()]
    if solve(line): p1 += 1
    else:
        for x in range(len(line)-1):
            y = copy.deepcopy(line)
            y.pop(-1)
            if solve(y): 
                p2+=1
                break
            z = copy.deepcopy(line)
            z.pop(x)
            if solve(z): 
                p2+=1
                break

print('P1: ', p1)
print('P2: ', p1+p2)