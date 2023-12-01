import time, os

def main():
    with open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp08.txt","r") as f:
        input = [line for line in f.read().split('\n')]  

    uniqueVals = [2,3,4,7]
    patterns, output = [], []

    #split raw input into a list of initial patterns, followed by a list of outputs
    for n in range(len(input)):
        patterns.append(input[n].split(' | ')[0].split(' '))
        output.append(input[n].split(' | ')[1].split(' '))

    p1 = 0
    for pattern in output:
        for segment in pattern:
            if len(segment) in uniqueVals: p1+=1

    displays = []
    for x, pattern in enumerate(patterns):
        signals = {}
        while len(signals) <= 9: #continue until all signals are populated
            for signal in pattern:
                if signal not in signals.values():
                    #populate values for unique numbers
                    if len(signal) == 2: signals['1'] = ''.join(sorted(signal))
                    elif len(signal) == 3: signals['7'] = ''.join(sorted(signal))
                    elif len(signal) == 4: signals['4'] = ''.join(sorted(signal))
                    elif len(signal) == 7: signals['8'] = ''.join(sorted(signal))
                    
                    elif '1' in signals.keys() and '4' in signals.keys():    
                        if len(signal) == 5: #check all 5 length signals
                            countIn1 = 0
                            countIn4 = 0
                            for segment in signal: #count how many sections this signal shares with '1' and '4'
                                if segment in signals.get('1'): countIn1 += 1
                                if segment in signals.get('4'): countIn4 += 1
                            if countIn1 == 2: signals['3'] = ''.join(sorted(signal)) #'3' is the only 5 length signal that shares all of '1'
                            elif countIn4 == 3: signals['5'] = ''.join(sorted(signal)) #'5' shares 3 sections with '4'
                            else: signals['2'] = ''.join(sorted(signal)) #if neither of the above, the signal must be '2'
                        
                        elif len(signal) == 6: #check all 6 length signals
                            countIn1 = 0
                            countIn4 = 0
                            for segment in signal: #count how many sections this signal shares with '1' and '4'
                                if segment in signals.get('1'): countIn1 += 1
                                if segment in signals.get('4'): countIn4 += 1
                            if countIn4 == 4: signals['9'] = ''.join(sorted(signal)) #'9' is the only 6 length signal that shares 4 sdegments with '4'
                            elif countIn1 == 2: signals['0'] = ''.join(sorted(signal)) #'2' is the only 6 length signal that shares all of '1'
                            else: signals['6'] = ''.join(sorted(signal)) #if neither of the above, the signal must be '6'
        
        display = '' #now that we know what each signal represents, we can calculate the output for this board
        for signal in output[x]:
            display+= list(signals.keys())[list(signals.values()).index(''.join(sorted(signal)))]          

        displays.append(int(display))

    print("Part 1:", p1)
    print("Part 2:", sum(displays))

if __name__ == "__main__": 
    startTime = time.time()
    main()
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))