import time, os

def main(input: list[list]):
    p1, p2 = 0, 0
    seen = []
    small_twice = False
       
    for x, path in enumerate(input): #we always check if [0] is start or [1] is end, so reverse any that are backwards
        if path[1] == 'start': input[x].reverse()
        if path[0] == 'end': input[x].reverse()

    #we can travel through a path either way, so for all non-start and non-end paths, add the reverse direction as an option
    temp_list = []
    for path in input:
        if 'start' not in path and 'end' not in path:
            temp_list.append([path[1], path[0]])

    for path in temp_list: input.append(path)
    
    for path in input:
        if path[0] == 'start':
            x, y = traverse(input, seen.copy(), path, small_twice)
            p1 += x 
            p2 += y

    print("Part 1:", p1)
    print("Part 2:", p2)

def traverse(input: list, seen: list, path: list[str,str], small_twice: bool):
    start, end = path[0], path[1]
    p1, p2 = 0, 0

    if end == 'end': return 1, 1 

    if start.islower():
        seen.append(start)
        if seen.count(start) > 1: small_twice = True
    
    for next_path in input:
        next_start = next_path[0]
        if end not in seen and end == next_start:
            x, y = traverse(input, seen.copy(), next_path, small_twice)
            p1 += x
            p2 += y
        elif seen.count(end) < 2 and end == next_start and not small_twice:
            p2 += traverse(input, seen.copy(), next_path, small_twice)[1]
        
    return p1, p2
        
if __name__ == "__main__": 
    start_time = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+"/inputs/inp12.txt","r") as f:
        input = [line.split('-') for line in f.read().split('\n')]
    main(input)
    print ('[Finished in {:.2f}s]'.format((time.time() - start_time)))