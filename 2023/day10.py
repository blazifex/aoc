from time import time
import re

startTime = time()

with open("inputs/inp10.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

for row, line in enumerate(INPUT):
    INPUT[row] = list(line)
    for col, char in enumerate(line):
        if char == 'S': start = [row, col]

path = []
def step(row, col, dr):
    global path
    path = []
    dist = 0
    while True:
        dist += 1
        if row < 0 or row > len(INPUT)-1: 
            dist = 0
            break
        elif col < 0 or col > len(INPUT[0])-1: 
            dist = 0
            break
        elif INPUT[row][col] == '.':
            path.append([row, col])
            break
        elif INPUT[row][col] == '|':
            path.append([row, col])
            if dr == 's':
                row += 1
            elif dr == 'n': 
                row -= 1
            else:
                path = []
                break
        elif INPUT[row][col] == '-':
            path.append([row, col])
            if dr == 'e': 
                col += 1
            elif dr == 'w': 
                col -= 1
            else: 
                path = []
                break
        elif INPUT[row][col] == 'L':
            path.append([row, col])
            if dr == 's': 
                col += 1
                dr = 'e'
            elif dr == 'w': 
                row -= 1
                dr = 'n'
            else: 
                path = []
                break
        elif INPUT[row][col] == 'J':
            path.append([row, col])
            if dr == 'e':
                row -= 1
                dr = 'n'
            elif dr == 's': 
                col -= 1
                dr = 'w'
            else: 
                path = []
                break
        elif INPUT[row][col] == '7':
            path.append([row, col])
            if dr == 'e': 
                row += 1
                dr = 's'
            elif dr == 'n': 
                col -= 1
                dr = 'w'
            else: 
                path = []
                break
        elif INPUT[row][col] == 'F':
            path.append([row, col])
            if dr == 'n': 
                col += 1
                dr = 'e'
            elif dr == 'w': 
                row += 1
                dr = 's'
            else:
                path = []
                break
        elif INPUT[row][col] == 'S':
            path.append([row, col])
            break
    return dist

step(start[0], start[1]+1, 'e') # check east of start
if len(path) == 0: step(start[0], start[1]-1, 'w') # check west of start
if len(path) == 0: step(start[0]-1, start[1], 'n') # check north of start
if len(path) == 0: step(start[0]+1, start[1], 's') # check south of start

#make printable
for n in path:
    row, col = n[0], n[1]
    INPUT[row][col] = INPUT[row][col].translate(str.maketrans("-|F7LJS", "─│┌┐└┘│")) # manually check which S should be replaced with by inspection

p2 = 0
for row, line in enumerate(INPUT):
    walls = 0
    for col, char in enumerate(line):
        if re.match (r'│|└|┘', char): # don't need to count ┌ or ┐ as they need to be paired with └ and ┘ to make a wall
            walls += 1
        elif walls % 2 == 1 and not re.match (r'─|│|┌|┐|└|┘', char): 
            INPUT[row][col] = 'I'
            p2+= 1
        elif not re.match (r'─|│|┌|┐|└|┘', char): INPUT[row][col] = 'O'
            
#for line in INPUT: print(''.join(line)) # print map for debugging

print(round(len(path)/2)) # part 1
print(p2) # part 2
print ('[Finished in {:.2f}ms]'.format(1000*(time() - startTime)))
