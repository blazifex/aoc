import time, os, math

def main():
    with open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp09.txt","r") as f:
        input = [line for line in f.read().split('\n')]
    
    low_points, basins, seen = [], [], []

    for row in range(len(input)):
        for col in range(len(input[row])):
            if ((col > 0 and input[row][col] >= input[row][col-1]) #check left of position
            or (col < len(input[row])-1 and input[row][col] >= input[row][col+1]) #check right of position
            or (row > 0 and input[row][col] >= input[row-1][col]) #check above position
            or (row < len(input)-1 and input[row][col] >= input[row+1][col])): #check below position
                continue

            low_points.append(int(input[row][col])) #add to list of low points for part 1 calc
            basins.append(checkBasin(input, row, col, seen)[0]) #check points around for basin size

    print("Part 1:",sum(low_points)+len(low_points))

    basins.sort()
    print("Part 2:", basins[-1]*basins[-2]*basins[-3])

def checkBasin(input: list, row, col, seen: list):
    count = 1
    if input[row][col] == '9' or str(row)+','+str(col) in seen:
        return 0, seen
    seen.append(str(row)+','+str(col))

    if col > 0 and input[row][col] < input[row][col-1]: #check left of position
        count+=checkBasin(input, row, col-1, seen)[0]
    if col < len(input[row])-1 and input[row][col] < input[row][col+1]: #check right of position
        count+=checkBasin(input, row, col+1, seen)[0]    
    if row > 0 and input[row][col] < input[row-1][col]: #check above position
        count+=checkBasin(input, row-1, col, seen)[0]
    if row < len(input)-1 and input[row][col] < input[row+1][col]: #check below position
        count+=checkBasin(input, row+1, col, seen)[0]

    return count, seen

if __name__ == "__main__": 
    startTime = time.time()
    main()
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))