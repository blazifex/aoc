import re, time

startTime = time.time()

with open("inputs/inp04.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

p1 = 0
cards = []
owned = [x for x in range(1, len(INPUT)+1)]

for id, line in enumerate(INPUT):
    nums = line.split(': ')[1].split('|')
    win = re.findall(r'(\d+)', nums[0])
    have = re.findall(r'(\d+)', nums[1])
    d = {'id': id+1, 'win': win, 'have': have, 'win_count': 0}
    val = 0
    win_count = 0

    for h in have:
        if h in win:
            win_count += 1
            if val == 0: val = 1
            else: val *= 2
    
    p1 += val
    d['win_count'] = win_count
    cards.append(d)

for id in owned:
    val = cards[id-1]['win_count']
    for x in range(1, val+1): owned.append(id+x)

print(p1) #part 1
print(len(owned)) #part 2

print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))