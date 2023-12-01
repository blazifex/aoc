import time, os

def main(coords: list[list], instructions: list[list]):
    p1 = 0

    found_max_x = False
    found_max_y = False
    for instruction in instructions: 
        if instruction[0] == 'x' and not found_max_x: 
            max_x = (int(instruction[1])*2)+1
            found_max_x = True
        if instruction[0] == 'y' and not found_max_y:
            max_y = (int(instruction[1])*2)+1
            found_max_y = True
        if found_max_x and found_max_y: break

    paper = []
    for _ in range(max_y): paper.append(['.'] * max_x)

    for coord in coords: paper[coord[1]][coord[0]] = "#"
    
    for x, instruction in enumerate(instructions):
        paper = fold(paper, instruction[0], int(instruction[1]))
        if x == 0 : p1+=sum(line.count('#') for line in paper)
    
    print("Part 1:", p1)
    print("Part 2:")

    print_paper(paper)

def fold(paper: list[list], axis, val: int):
    new_paper = []
    
    if axis == 'y':
        top_paper, bottom_paper = [], []

        for line in paper[:val]: top_paper.append(line)
        for line in paper[val+1:]: bottom_paper.append(line)
        bottom_paper.reverse()
        
        for line in range(len(top_paper)):
            paper_line = []
            for char in range(len(top_paper[0])):
                if top_paper[line][char] == '#' or bottom_paper[line][char] == '#':
                    paper_line.append('#')
                else: paper_line.append('.')
            new_paper.append(paper_line)

    if axis == 'x':
        left_paper, right_paper = [], []

        for line in paper:
            left_line, right_line = [], []
            
            for char in line[:val]: left_line.append(char)
            left_paper.append(left_line)

            for char in line[val+1:]: right_line.append(char)
            right_paper.append(list(reversed(right_line)))

        for line in range(len(paper)):
            paper_line = []
            for char in range(len(left_paper[0])):
                if left_paper[line][char] == '#' or right_paper[line][char] == '#':
                    paper_line.append("#")
                else: paper_line.append('.')
                
            new_paper.append(paper_line)

    return new_paper

def print_paper(paper: list[list]):
    for line in paper:
        line_str = ''
        for char in line:
            line_str += str(char)
        print(line_str)

if __name__ == "__main__": 
    start_time = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+"/inputs/inp13.txt","r") as f:
        input = [line for line in f.read().split('\n\n')]
    coords = [list(map(int, line.split(','))) for line in input[0].split('\n')]
    instructions = [line.strip('fold along ').split('=') for line in input[1].split('\n')]
    main(coords, instructions)
    print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))