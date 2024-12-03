import re

with open("inp03.txt") as fh: 
    lines = fh.read().strip().split('\n')

p1, p2 = 0, 0
line = ''
enabled = []

for x in lines:
    line += x

def calc(line: str):
    ans = 0
    for x in re.findall(r'mul\([0-9]+\,[0-9]+\)', line):
        i, j = map(int, re.findall('[0-9]+', x)[:2])
        ans += i * j
    return ans

p1 += calc(line)
enabled += re.findall(r'(?=^|do\(\)).*?(?=don\'t\(\)|$)', line)
for x in enabled:
    p2 += calc(x)

print('P1: ', p1)
print('P2: ', p2)