import re

with open("inputs/inp03.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

pattern = r'[^\d\.]'
p1, p2 = [], []
nums = []
chars = []
num_index = 0
char_index = 0

for line_id, line in enumerate(INPUT):
    results = re.finditer('\d+', line)
    for result in results:
        d = {'id': num_index, 'val': result.group(), 'row': line_id, 'col_start': result.start(), 'col_end': result.end()-1}
        num_index+=1
        nums.append(d)
    
    results = re.finditer('[^\d\.]', line)
    for result in results:
        d = {'id': char_index, 'val': result.group(), 'row': line_id, 'col': result.start()}
        char_index+=1
        chars.append(d)

for num in nums:
    for char in chars:
        if char['row'] == num['row']:
            if num['col_start'] == char['col']+1: p1.append(int(num['val'])) #if char is just before num
            if num['col_end'] == char['col']-1: p1.append(int(num['val'])) #if char is just after num
        if char['row'] == num['row']+1:
            if num['col_start']-1 <= char['col'] <= num['col_end']+1: p1.append(int(num['val'])) #if char is below number, incl. adjacent
        if char['row'] == num['row']-1:
            if num['col_start']-1 <= char['col'] <= num['col_end']+1: p1.append(int(num['val'])) #if char is above number, incl. adjacent

for char in chars:
    if char['val'] == '*': 
        adj_count = 0
        adj = []
        for num in nums:
            if char['row'] == num['row']:
                if num['col_start'] == char['col']+1: #if char is just before num
                    adj.append(int(num['val'])) 
                    adj_count+=1
                if num['col_end'] == char['col']-1: #if char is just after num
                    adj.append(int(num['val'])) 
                    adj_count+=1
            if char['row'] == num['row']+1:
                if num['col_start']-1 <= char['col'] <= num['col_end']+1: #if char is below number, incl. adjacent
                    adj.append(int(num['val'])) 
                    adj_count+=1
            if char['row'] == num['row']-1:
                if num['col_start']-1 <= char['col'] <= num['col_end']+1: #if char is above number, incl. adjacent
                    adj.append(int(num['val'])) 
                    adj_count+=1
        if adj_count == 2:
            result = 1
            for num in adj:
                result *= num
            p2.append(result)

print(sum(p1))
print(sum(p2))