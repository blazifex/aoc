import time, math

start_time = time.time()
p1, p2 = [], []

with open("inputs/inp06.txt") as fh:
    input = fh.read().strip().split('\n')

operations = input[-1].split()

# prepare part 1 input
for n, problem in enumerate(input[:-1]):
    numbers = problem.split()
    p1.append(int(x) for x in numbers)

p1 = list(zip(*p1))

# prepare part 2 input
p2 = input[:-1]
p2 = list(zip(*p2))
p2.reverse()

for n, problem in enumerate(p2):
    number = ''
    for char in problem:
        if char != ' ': number += char
    if number != '': 
        p2[n] = int(number)
    if not isinstance(p2[n], int): p2[n] = 'x'

p2_clean = []
temp = []

for problem in p2:
    if problem == 'x':
        p2_clean.append(temp)
        temp = []
    else: temp.append(problem)
p2_clean.append(temp)    

p2 = p2_clean
p2.reverse()

# solve
def calc(problems):
    ans = 0
    for n, problem in enumerate(problems):
        if operations[n] == '*':
            ans += math.prod(problem)
        elif operations[n] == '+':
            ans += sum(problem)
    return ans

print("P1: ", calc(p1))
print("P2: ", calc(p2))
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))