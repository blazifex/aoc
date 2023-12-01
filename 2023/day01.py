with open("inputs/inp01.txt") as fh:
    lines = fh.read().split('\n')

def calibrate(lines):
    values = []
    for line in lines:
        first, last = 0,0
        for char in line:
            if char.isnumeric():
                first = char
                break
        for char in reversed(line):
            if char.isnumeric():
                last = char
                break
        values.append(int(str(first)+str(last)))
    return values

p2 = []
for line in lines:
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    p2.append(line)

print(sum(calibrate(lines))) # part 1
print(sum(calibrate(p2))) # part 2