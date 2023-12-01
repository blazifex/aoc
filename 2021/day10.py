import time, os

def main():
    with open(os.path.dirname(os.path.abspath(__file__))+"/inputs/inp10.txt","r") as f:
        input = [line for line in f.read().split('\n')]

    openings = ['[', '{', '(', '<']
    closings = [']', '}', ')', '>']
    pairings = dict(zip(openings, closings))
    
    p1, p2 = 0, []
    p1_score = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
    p2_score = { ')': 1, ']': 2, '}': 3, '>': 4 }

    for line in input:
        expected = []
        badLine = False

        for char in line:
            if char in openings:
                expected.insert(0, pairings[char])
            if char in closings:
                if char != expected.pop(0):
                    p1 += p1_score[char]
                    badLine = True
                    break
        
        if not badLine:
            score = 0
            for char in expected:
                score = (score*5) + p2_score[char]
            p2.append(score)   

    p2.sort()

    print("Part 1:", p1)
    print("Part 2:", p2[int(len(p2)/2)])

if __name__ == "__main__": 
    startTime = time.time()
    main()
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))