import re

with open("inputs/inp02.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')
    games = [line.split(": ") for line in INPUT]

p1, p2 = [], []
r_min, g_min, b_min = 12, 13, 14

for game, pulls in games:
    d = {'id': re.search('\d+', game).group(0), 'blue': 0, 'red': 0, 'green': 0}
    red, green, blue = [], [], []
    pattern = r'(\d+) (red|green|blue)'
    for pull in pulls.split(';'):
        for count, colour in re.findall(pattern, pull): 
            if int(count) > d[colour]: d[colour] = int(count)

    if d['red'] <= r_min and d['green'] <= g_min and d['blue'] <= b_min: p1.append(int(d['id']))
    p2.append(d['blue']*d['red']*d['green'])

print(sum(p1))
print(sum(p2))