import time, os

def main():
    startTime = time.time()
    commands = parseCommands([line.rstrip() for line in open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp02.txt","r").read().split('\n')])

    print("Part 1: ", p1(commands, 0, 0))
    print("Part 2: ", p2(commands, 0, 0, 0))
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))

def parseCommands(inp):
    commands = []
    for n in range(len(inp)):
        commands.append([inp[n].split(" ")[0], int(inp[n].split(" ")[1])])
    return commands

def p1(inp, hPos, depth):
    for n in range(len(inp)):
        if(inp[n][0] == "forward"): hPos+= inp[n][1]
        elif(inp[n][0] == "down"): depth+= inp[n][1]
        elif(inp[n][0] == "up"): depth-= inp[n][1]
    return hPos*depth

def p2(inp, aim, hPos, depth):
    for n in range(len(inp)):
        if(inp[n][0] == "forward"): 
            hPos+= inp[n][1]
            depth+= aim*inp[n][1]
        elif(inp[n][0] == "down"): aim+= inp[n][1]
        elif(inp[n][0] == "up"): aim-= inp[n][1]
    return hPos*depth    

if __name__ == "__main__": main()