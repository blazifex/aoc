import re, time

startTime = time.time()

with open("inputs/inp04.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

p1 = 0
cards = []
owned = []

for id, line in enumerate(INPUT):
    nums = line.split(': ')[1]
    nums = nums.split('|')
    
    win = re.findall(r'(\d+)', nums[0])
    have = re.findall(r'(\d+)', nums[1])
    d = {'id': id+1, 'win': win, 'have': have}
    cards.append(d)
    
    val = 0
    for h in have:
        for w in win:
            if h == w:
                if val == 0: val = 1
                else: val *= 2
    p1+= val

x = 0
while x < len(cards):
    x+=1
    owned.append(x)

for id in owned:
    for card in cards:
        if card['id'] == id:
            val = 0
            for h in card['have']:
                for w in card['win']:
                    if h == w: val+=1
            x = 1
            while x <= val:
                owned.append(id+x)
                x+=1

print(p1)
print(len(owned))
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))
