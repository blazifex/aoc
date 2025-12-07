import time, math

start_time = time.time()
p1, p2 = 0, 0

with open("inputs/inp07.txt") as fh:
    input = fh.read().strip().split('\n')

for r, row in enumerate(input):
    row_list = []
    for char in row:
        row_list.append(char)
    input[r] = row_list

def is_valid(row, col):
    if len(input)-1 >= row >= 0 and len(input[0])-1 >= col >= 0: return True
    return False

for r, row in enumerate(input):
    for c, col in enumerate(row):
        if col != '^' and col != '.':
            if is_valid(r+1, c) and input[r+1][c] != '^': 
                if col == 'S': input[r+1][c] = 1
                elif input[r+1][c] == '.': input[r+1][c] = col
                else: input[r+1][c] += col

            elif is_valid(r+1, c) and input[r+1][c] == '^':
                if is_valid(r+1, c-1): 
                    if input[r+1][c-1] == '.': input[r+1][c-1] = col
                    elif input[r+1][c-1] != '^': input[r+1][c-1] += col
                if is_valid(r+1, c+1): 
                    if input[r+1][c+1] == '.': input[r+1][c+1] = col
                    elif input[r+1][c+1] != '^': input[r+1][c+1] += col
                p1 += 1
        
for char in input[-1]: 
    if char != '.': p2 += char

print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))