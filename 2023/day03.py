import re

with open("inputs/inp03.txt") as fh:
    INPUT = fh.read().rstrip().split('\n')

pattern = r'[^\d\.]'
p1, p2 = [], []

for line_id, line in enumerate(INPUT):
    if re.findall('\d+', line):
        nums = re.findall('\d+', line)
        for num in nums:
            num_only = r'(?<!\d)' + num + '(?!\d)'
            loc = re.search(num_only, line).span()
            for char_id, char in enumerate(line):
                if loc[1]-1 >= char_id >= loc[0]: 
                    if char_id > 0 and re.match(pattern, line[char_id-1]): #check characters before on same line
                        p1.append(int(num))
                        break
                    if char_id < len(line)-1 and re.match(pattern, line[char_id+1]): #check characters after on same line
                        p1.append(int(num))
                        break
                    if line_id > 0 and re.match(pattern, INPUT[line_id-1][char_id]): #check characters above
                        p1.append(int(num))
                        break
                    if line_id < len(INPUT)-1 and re.match(pattern, INPUT[line_id+1][char_id]): #check characters below
                        p1.append(int(num))
                        break
                    if line_id < len(INPUT)-1 and char_id > 0 and re.match(pattern, INPUT[line_id+1][char_id-1]): #check characters diagonally left and down
                        p1.append(int(num))
                        break
                    if line_id < len(INPUT)-1 and char_id < len(line)-1 and re.match(pattern, INPUT[line_id+1][char_id+1]): #check characters diagonally right and down
                        p1.append(int(num))
                        break
                    if line_id > 0 and char_id > 0 and re.match(pattern, INPUT[line_id-1][char_id-1]): #check characters diagonally left and up
                        p1.append(int(num))
                        break
                    if line_id > 0 and char_id < len(line)-1 and re.match(pattern, INPUT[line_id-1][char_id+1]): #check characters diagonally right and up
                        p1.append(int(num))
                        break
                
print(sum(p1))
print(sum(p2))