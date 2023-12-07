import re, numpy as np

with open("inputs/inp07.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

hands = [line.split() for line in INPUT]
power = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

p1 = 0

fives = [] # five of a kind
fours = [] # four of a kind
fulls = [] # full house
threes = [] # three of a kind
twos = [] # two pair
ones = [] # one pair
high = [] # high card


for h in hands:
    h[0] = h[0].translate(str.maketrans('TJQKA', 'ABCDE'))
    x = ''.join(sorted(h[0]))
    if re.search(r'(.)\1{4,}', x): fives.append(h) # check 5 of a kind
    elif re.search(r'(.)\1{3,}', x): fours.append(h) # check 4 of a kind
    elif re.search(r'(.)\1{2,}(.)\2{1,}', x) or re.search(r'(.)\1{1,}(.)\2{2,}', x):  fulls.append(h) # check full house
    elif re.search(r'(.)\1{2,}', x): threes.append(h) # check 3 of a kind
    elif re.search(r'^(?=.*(.).*?\1)(?=.*(?!\1)(.).*?\2).*', x):  twos.append(h) # check two pairs
    elif re.search(r'(.)\1{1,}', x): ones.append(h) # check one pair
    else: high.append(h)

combined = sorted(high)+sorted(ones)+sorted(twos)+sorted(threes)+sorted(fulls)+sorted(fours)+sorted(fives)
#print(combined)
for id, h in enumerate(combined): p1+= int(h[1])*(id+1)

print(p1)

"""                 PART 2                  """

fives = [] # five of a kind
fours = [] # four of a kind
fulls = [] # full house
threes = [] # three of a kind
twos = [] # two pair
ones = [] # one pair
high = [] # high card

for h in hands:
    h[0] = h[0].translate(str.maketrans('ABCDE', 'TJQKA'))
    h[0] = h[0].translate(str.maketrans('TQKAJ', 'ABCD1'))
    x = ''.join(sorted(h[0]))
    if re.search(r'(.)\1{4,}', x): fives.append(h) # check 5 of a kind
    elif re.search(r'(.)\1{3,}', x): # check 4 of a kind
        if x.count('1') > 0: fives.append(h)
        else: fours.append(h)
    elif re.search(r'(.)\1{2,}(.)\2{1,}', x) or re.search(r'(.)\1{1,}(.)\2{2,}', x): # check full house  
        if x.count('1') > 0: fives.append(h)
        else: fulls.append(h)
    elif re.search(r'(.)\1{2,}', x): # check 3 of a kind
        if x.count('1') == 1 or x.count('1') == 3: fours.append(h)
        else: threes.append(h) 
    elif re.search(r'^(?=.*(.).*?\1)(?=.*(?!\1)(.).*?\2).*', x): # check two pairs
        if x.count('1') == 1: fulls.append(h)
        elif x.count('1') == 2: fours.append(h)
        else: twos.append(h)
    elif re.search(r'(.)\1{1,}', x): # check one pair
        if x.count('1') == 1: threes.append(h)
        else: ones.append(h)
    else: 
        if x.count('1') == 1: ones.append(h)
        else: high.append(h)

combined = sorted(high)+sorted(ones)+sorted(twos)+sorted(threes)+sorted(fulls)+sorted(fours)+sorted(fives)

p2 = 0
for id, h in enumerate(combined):
    #h[0] = h[0].translate(str.maketrans('ABCD1', 'TQKAJ'))
    #print(h)
    p2+= int(h[1])*(id+1)

print(p2)