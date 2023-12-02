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
    line = (line.replace("one", "o1e")
    .replace("two", "t2o")
    .replace("three", "t3e")
    .replace("four", "f4r")
    .replace("five", "f5e")
    .replace("six", "s6x")
    .replace("seven", "s7n")
    .replace("eight", "e8t")
    .replace("nine", "n9e"))
    p2.append(line)

print(sum(calibrate(lines))) # part 1
print(sum(calibrate(p2))) # part 2