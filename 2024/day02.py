import copy
with open("inp02.txt") as fh: 
    lines = fh.read().strip().split('\n')

p1, p2 = 0, 0

def is_safe(line: list):
    if line == sorted(line) or line == sorted(line, reverse=True):
        for x in range(len(line)-1):
            if not 1 <= (abs(line[x] - line[x+1])) <= 3: return False
        return True
    else: return False

for line in lines:
    line = [int(x) for x in line.split()]
    x = copy.deepcopy(line)
    x.pop(-1)
    if is_safe(line): p1+=1
    elif is_safe(x): p2+=1
    else:
        for n in range(len(line)-1):
            y = copy.deepcopy(line)
            y.pop(n)
            if is_safe(y): 
                p2+=1
                break

print('P1: ', p1)
print('P2: ', p1+p2)