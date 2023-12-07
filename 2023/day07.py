import re
from time import time as time
from copy import deepcopy as copy

def main():
    startTime = time()

    with open("inputs/inp07.txt") as fh:
        INPUT = fh.read().rstrip().split('\n')

    hands = [line.split() for line in INPUT]
    
    print(calc(hands, False)) # part 1
    print(calc(hands, True)) # part 2
    print ('[Finished in {:.2f}ms]'.format(1000*(time() - startTime)))

def calc(hands: list[str, str], joker_rule: bool):
    fives = [] # five of a kind
    fours = [] # four of a kind
    fulls = [] # full house
    threes = [] # three of a kind
    twos = [] # two pair
    ones = [] # one pair
    high = [] # high card

    hands = copy(hands)

    for h in hands:
        h[0] = h[0].translate(str.maketrans('TJQKA', 'ABCDE'))
        if joker_rule: h[0] = h[0].translate(str.maketrans('B', '1')) # replace jokers (previously changed to B) to 1 to sort @ end
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
            if x.count('1') == 1 or x.count('1') == 2: threes.append(h)
            else: ones.append(h)
        
        else: # high card
            if x.count('1') == 1: ones.append(h)
            else: high.append(h)

    combined = sorted(high)+sorted(ones)+sorted(twos)+sorted(threes)+sorted(fulls)+sorted(fours)+sorted(fives)
    val = 0
    for id, h in enumerate(combined): val+= int(h[1])*(id+1)
    return val

if __name__ == "__main__": main()