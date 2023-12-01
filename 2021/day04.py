import time, os

def main():
    startTime = time.time()
    with open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp04.txt","r") as inpFile:
        inp = [line.rstrip() for line in inpFile.read().split('\n\n')]

    #populate draw
    draw = inp[0].split(',')  
    #populate cards
    cards=[]
    for n in range(1, len(inp)):
        inp[n] = inp[n].replace('  ', ' ')
        cards.append(inp[n].split('\n'))
    for i in range(len(cards)):
        for j in range(len(cards[i])):
            cards[i][j] = cards[i][j].split(' ')
            if cards[i][j][0] == '': cards[i][j].pop(0)

    #populate list of rows
    cardRows = cards

    #populate list of columns
    cardCols = []
    for card in range(len(cards)):
        cardCols.append(list(map(list, zip(*cards[card]))))
  
    winningCards = []
    winningDraw = []
    drawn = draw[:4]
    for ball in range(4, len(draw)):
        drawn.append(draw[ball])
        for card in range(len(cards)):
            if card not in winningCards:
                for x in range(len(cardRows[card])):
                    win = False
                    rowWin, colWin = 0, 0
                    for element in range(len(cardRows[card][x])):
                        if cardRows[card][x][element] in drawn: rowWin +=1
                        if cardCols[card][x][element] in drawn: colWin +=1
                    if rowWin == 5 or colWin == 5:
                        winningCards.append(card)
                        winningDraw.append(drawn.copy())
                        win = True
                if win == True: break

    #output
    print("Part 1:", calcs(cards[winningCards[0]], winningDraw[0]))
    print("Part 2:", calcs(cards[winningCards[-1]], winningDraw[-1]))
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))

def calcs(card, draw):
    unmarked = []
    for x in range(len(card)):
        for y in range(len(card[x])):
            if card[x][y] not in draw: 
                unmarked.append(int(card[x][y]))
    return sum(unmarked)*int(draw[-1])

if __name__ == "__main__": main()