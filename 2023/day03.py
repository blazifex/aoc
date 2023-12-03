import re, time

def main():
    startTime = time.time()
    with open("inputs/inp03.txt") as fh:
        INPUT = fh.read().rstrip().split('\n')

    nums, chars = [], []

    for line_id, line in enumerate(INPUT):
        parse(line_id, re.finditer('\d+', line), nums)
        parse(line_id, re.finditer('[^\d\.]', line), chars)
    p1(nums, chars)
    p2(nums, chars)
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))

def parse(line_id, results, arr):
    for result in results:
        d = {'val': result.group(), 'row': line_id, 'col_start': result.start(), 'col_end': result.end()-1}
        arr.append(d)

def check_adj(num, char):
    if char['row'] == num['row']:
            if num['col_start'] == char['col_start']+1: return True #if char is just before num
            if num['col_end'] == char['col_start']-1: return True #if char is just after num
    if char['row'] == num['row']+1:
        if num['col_start']-1 <= char['col_start'] <= num['col_end']+1: return True #if char is below number, incl. adjacent
    if char['row'] == num['row']-1:
        if num['col_start']-1 <= char['col_start'] <= num['col_end']+1: return True #if char is above number, incl. adjacent
    return False


def p1(nums, chars, arr = []):
    for num in nums:
        for char in chars:
            if check_adj(num, char): arr.append(int(num['val']))
    print(sum(arr))

def p2(nums, chars, arr = []):
    for char in chars:
        if char['val'] == '*': 
            adj_count = 0
            adj = []
            for num in nums:
                if check_adj(num, char):
                    adj.append(int(num['val'])) 
                    adj_count+=1
            if adj_count == 2:
                result = 1
                for num in adj:
                    result *= num
                arr.append(result)
    print(sum(arr))

if __name__ == "__main__": main()