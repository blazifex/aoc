import time

start_time = time.time()
p1, p2 = 0, 0

with open("inputs/inp04.txt") as fh:
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
        if col != '.':
            neighbours = 0
            # | +1, 0 | +1, +1 | +1, -1 | -1, 0 | -1, +1 | -1, -1 | 0, -1 | 0, +1 |
            if is_valid(r+1, c): #1
                if input[r+1][c] != '.': neighbours += 1
            if is_valid(r+1, c+1): #2
                if input[r+1][c+1] != '.': neighbours += 1
            if is_valid(r+1, c-1): #3
                if input[r+1][c-1] != '.': neighbours += 1
            if is_valid(r-1, c): #4
                if input[r-1][c] != '.': neighbours += 1
            if is_valid(r-1, c+1): #5
                if input[r-1][c+1] != '.': neighbours += 1
            if is_valid(r-1, c-1): #6
                if input[r-1][c-1] != '.': neighbours += 1
            if is_valid(r, c-1): #7
                if input[r][c-1] != '.': neighbours += 1
            if is_valid(r, c+1): #8
                if input[r][c+1] != '.': neighbours += 1
            if neighbours < 4: 
                input[r][c] = 'x'
                p1 += 1

"""for row in input:
    row_string = ''
    for col in row:
        row_string += col
    print(row_string)"""
    

print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))