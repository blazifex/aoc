import time, os, re
from collections import Counter

def main(poly: list, rules: dict):
    p1, p2 = 0, 0
    p1_steps = 10
    p2_steps = 40
    pairs = Counter()

    #initial count of pairs
    for n in range(len(poly)-1):
        pairs[poly[n]+poly[n+1]] += 1
    
    for step in range(p2_steps):
        c = Counter()

        if step == p1_steps: p1 = get_solution(pairs, poly)

        #if the rule is "AB -> C", AB becomes AC, CB
        for pair in pairs:
            c[pair[0]+rules[pair]] += pairs[pair] #you'd have count(AB) amount of AC's being created
            c[rules[pair]+pair[1]] += pairs[pair] #you'd also have count(AB) amount of CB's being created
        
        pairs = c

    p2 = get_solution(pairs, poly)

    print("Part 1:", p1)
    print("Part 2:", p2)

def get_solution(pairs: Counter, poly: list):
    c = Counter()
    for n in pairs:             #count only the instances of the first character in each pair, 
        c[n[0]] += pairs[n]     #so we don't double count the second character
    
    c[poly[-1]] += 1    #as we're only counting the first character of each pair, the final character is left out, 
                        #which is always the same as the final charactger of the original string

    return max(c.values()) - min(c.values())

def parse_input(input):
    poly = list(input[0])
    rule_list = input[1].split('\n')
    rules: dict = {}
    for line in rule_list:
        rule = re.search(r"([A-Z]{2}) -> ([A-Z])", line) #could also have just .split(' -> ') but I wanted to learn regex
        assert rule
        rules[rule.group(1)] = rule.group(2)

    return poly, rules

if __name__ == "__main__": 
    start_time = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+"/inputs/inp14.txt","r") as f:
        input = [line.strip() for line in f.read().split('\n\n')]
    
    poly, rules = parse_input(input)
    main(poly, rules)
    print ('[Finished in {:.3f}ms]'.format(1000*(time.time() - start_time)))