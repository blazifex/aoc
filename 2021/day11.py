import time, os

def main():
    with open(os.path.dirname(os.path.realpath(__file__))+"/inputs/inp11.txt","r") as f:
        input = [list(line) for line in f.read().split('\n')]

    step, p1, p2 = 0, 0, 0
    p1_steps = 100
    all_flashed = False

    while not all_flashed:
        for row, line in enumerate(input):
            for col, char in enumerate(line):
                if step < p1_steps: p1+=flash(input, row, col)
                else: flash(input, row, col)
        
        all_flashed = True
        for row, line in enumerate(input):
            for col, char in enumerate(line):        
                if char == 'f': input[row][col] = '0'
                else: all_flashed = False
        
        step = step+1
        if all_flashed: 
            p2 = step
            break

    print("Part 1:", p1)
    print("Part 2:", p2)

def flash(input: list, row, col):
    char = input[row][col]
    flashes = 0
    if char == 'f': return flashes
    if char != '9': input[row][col] = str(int(char)+1)
    else: 
        input[row][col] = 'f'
        flashes+=1
        checks = [[row-1,col-1],[row-1,col],[row-1,col+1],[row,col-1],[row,col+1],
        [row+1,col-1],[row+1,col],[row+1,col+1]]
        for check in checks:
            if 0 <= check[0] < len(input):
                if 0 <= check[1] < len(input[row]):
                    flashes+=flash(input, check[0], check[1])
    return flashes

if __name__ == "__main__": 
    startTime = time.time()
    main()
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))