import time, os

def main():
    with open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp05.txt","r") as inpFile:
        instructions = [line.rstrip() for line in inpFile.read().split('\n')]

    #process input
    allX = []
    allY = []
    for line in (range(len(instructions))):
        instructions[line] = instructions[line].split(' -> ')
        for coords in range(len(instructions[line])):
            allX.append(int(instructions[line][coords].split(',')[0]))
            allY.append(int(instructions[line][coords].split(',')[1]))

    #get max X and max Y value
    diagRows = max(allX)
    diagCols = max(allY)

    #populate initial diagram
    diagram = []   
    for _ in range(diagRows+1):
        row = []
        for _ in range(diagCols+1):
            row.append('.') 
        diagram.append(row)

    #process instructions
    for line in range(len(instructions)):
        x1 = int(instructions[line][0].split(',')[0])
        y1 = int(instructions[line][0].split(',')[1])
        x2 = int(instructions[line][1].split(',')[0])
        y2 = int(instructions[line][1].split(',')[1])

        if x1 == x2 or y1 == y2: #straight lines
            #determine biggest/smallest x value to iterate
            bigX, smallX = x1, x1
            if x1 < x2: bigX, smallX = x2, x1
            elif x1 > x2: bigX, smallX = x1, x2
            #determine biggest/smallest y value to iterate
            bigY, smallY = y1, y1
            if y1 < y2: bigY, smallY = y2, y1
            elif y1 > y2: bigY, smallY = y1, y2

            for x in range(smallY, bigY+1):
                for y in range(smallX, bigX+1):
                    if diagram[x][y] == '.': diagram[x][y] = '1'
                    else: diagram[x][y] = int(diagram[x][y])+1
        else: #diagonals
            xmod, ymod = 1, 1
            if x1 > x2: xmod = -1
            if y1 > y2: ymod = -1
            countX, countY = x1, y1

            for _ in range (abs(x1-x2)+1):
                for _ in range(abs(y1-y2)+1):
                    if diagram[countY][countX] == '.':
                        diagram[countY][countX] = '1'
                        break
                    else: 
                        diagram[countY][countX] = int(diagram[countY][countX])+1
                        break
                countX += xmod
                countY += ymod

    print(countOverlaps(diagram))

def countOverlaps(diagram): #counts number of overlaps
    overlaps = 0
    for row in range(len(diagram)):
        for col in range(len(diagram[row])):
            if diagram[row][col] != '.':
                if int(diagram[row][col]) > 1: overlaps+=1
    return overlaps

def printDiagram(diagram): #prints the current state of the diagram
    for row in range(len(diagram)):
        rowStr = ''
        for col in range(len(diagram[row])):
            rowStr += str(diagram[row][col])
        print(rowStr)

if __name__ == "__main__": 
    startTime = time.time()
    main()
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))