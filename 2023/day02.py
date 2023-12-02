import re

with open("inputs/inp02.txt") as fh:
    lines = fh.read().split('\n')
    games = [line.split(": ") for line in lines]

p1, p2 = [], []
r_min, g_min, b_min = 12, 13, 14

for game, pulls in games:
    d = {'id': re.search('\d+', game).group(0), 'blue': 0, 'red': 0, 'green': 0}
    pulls = [pull.split(', ') for pull in pulls.split('; ')]
    red, green, blue = [], [], []
    for pull in pulls:
        for cube in pull:
            if re.search('red', cube):
                red.append(int(re.search('\d+', cube).group(0)))
            if re.search('green', cube):
                green.append(int(re.search('\d+', cube).group(0)))
            if re.search('blue', cube):
                blue.append(int(re.search('\d+', cube).group(0)))
    d['red'] = max(red)
    d['green'] = max(green)
    d['blue'] = max(blue)
    if d['red'] <= r_min and d['green'] <= g_min and d['blue'] <= b_min: p1.append(int(d['id']))
    p2.append(d['blue']*d['red']*d['green'])

print(sum(p1))
print(sum(p2))