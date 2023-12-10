from time import time
import re

startTime = time()

with open("inputs/inp10.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

for r, line in enumerate(INPUT):
    INPUT[r] = list(line)
    for c, char in enumerate(line):
        if char == 'S': start = [r, c]

path = []
def step(r, c, d):
    global path
    path = []
    while True:
        if r < 0 or r > len(INPUT)-1: break
        elif c < 0 or c > len(INPUT[0])-1: break
        elif INPUT[r][c] == '.':
            path.append([r, c])
            break
        elif INPUT[r][c] == '|':
            path.append([r, c])
            if d == 's':
                r += 1
            elif d == 'n': 
                r -= 1
            else:
                path = []
                break
        elif INPUT[r][c] == '-':
            path.append([r, c])
            if d == 'e': 
                c += 1
            elif d == 'w': 
                c -= 1
            else: 
                path = []
                break
        elif INPUT[r][c] == 'L':
            path.append([r, c])
            if d == 's': 
                c += 1
                d = 'e'
            elif d == 'w': 
                r -= 1
                d = 'n'
            else: 
                path = []
                break
        elif INPUT[r][c] == 'J':
            path.append([r, c])
            if d == 'e':
                r -= 1
                d = 'n'
            elif d == 's': 
                c -= 1
                d = 'w'
            else: 
                path = []
                break
        elif INPUT[r][c] == '7':
            path.append([r, c])
            if d == 'e': 
                r += 1
                d = 's'
            elif d == 'n': 
                c -= 1
                d = 'w'
            else: 
                path = []
                break
        elif INPUT[r][c] == 'F':
            path.append([r, c])
            if d == 'n': 
                c += 1
                d = 'e'
            elif d == 'w': 
                r += 1
                d = 's'
            else:
                path = []
                break
        elif INPUT[r][c] == 'S':
            path.append([r, c])
            break

step(start[0], start[1]+1, 'e') # check east of start
if len(path) == 0: step(start[0], start[1]-1, 'w') # check west of start
if len(path) == 0: step(start[0]-1, start[1], 'n') # check north of start
if len(path) == 0: step(start[0]+1, start[1], 's') # check south of start

#make printable
for n in path:
    r, c = n[0], n[1]
    INPUT[r][c] = INPUT[r][c].translate(str.maketrans("-|F7LJS", "─│┌┐└┘│")) # manually check which S should be replaced with by inspection

p2 = 0
for r, line in enumerate(INPUT):
    walls = 0
    for c, char in enumerate(line):
        if re.match (r'│|└|┘', char): # don't need to count ┌ or ┐ as they need to be paired with └ and ┘ to make a wall
            walls += 1
        elif walls % 2 == 1 and not re.match (r'─|│|┌|┐|└|┘', char): 
            #INPUT[r][c] = 'I' # for easier print debugging
            p2+= 1
        #elif not re.match (r'─|│|┌|┐|└|┘', char): INPUT[r][c] = 'O' # for easier print debugging
            
#for line in INPUT: print(''.join(line)) # print map for debugging

print(round(len(path)/2)) # part 1
print(p2) # part 2
print ('[Finished in {:.2f}ms]'.format(1000*(time() - startTime)))
