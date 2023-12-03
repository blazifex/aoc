import re, time

def main():
    startTime = time.time()
    with open("inputs/inp03.txt") as fh:
        INPUT = fh.read().rstrip().split('\n')

    nums, chars = [], []

    for line_id, line in enumerate(INPUT):
        nums.extend(parse(line_id, re.finditer('\d+', line)))
        chars.extend(parse(line_id, re.finditer('[^\d\.]', line)))

    p1(nums, chars)
    p2(nums, chars)
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))

def parse(line_id: int, results: list[re.Match]):
    arr = []
    for result in results:
        d = {'val': result.group(), 'row': line_id, 'col_start': result.start(), 'col_end': result.end()-1}
        arr.append(d)
    return arr

def check_adj(num: dict, char: dict):
    if char['row'] == num['row']: #if char is on same row as num
        if num['col_start'] == char['col_start']+1: return True #if char is just before num
        if num['col_end'] == char['col_start']-1: return True #if char is just after num
    elif char['row'] == num['row']+1 or char['row'] == num['row']-1: #if char is above or below number
        if num['col_start']-1 <= char['col_start'] <= num['col_end']+1: return True #check if overlapping or adjacent column
    else: return False
    return False

def p1(nums: list, chars: list):
    p1 = 0
    for num in nums:
        for char in chars:
            if check_adj(num, char): p1 += int(num['val'])
    print(p1)

def p2(nums: list, chars: list):
    p2 = 0
    for char in chars:
        if char['val'] == '*': 
            adj_count = 0
            adj = []
            for num in nums:
                if check_adj(num, char):
                    adj.append(int(num['val'])) 
                    adj_count+=1
                    if adj_count > 2: break
            if adj_count == 2:
                result = 1
                for num in adj:
                    result *= num
                p2 += result
    print(p2)

if __name__ == "__main__": main()