import time

startTime = time.time()

with open("inputs/inp05.txt") as fh:
    INPUT = fh.read().rstrip().split('\n\n')
    
seeds = INPUT[0].split(':')[1].split()
seed_soil = INPUT[1].split('\n')[1:]
soil_fert = INPUT[2].split('\n')[1:]
fert_water = INPUT[3].split('\n')[1:]
water_light = INPUT[4].split('\n')[1:]
light_temp = INPUT[5].split('\n')[1:]
temp_humid = INPUT[6].split('\n')[1:]
humid_loc = INPUT[7].split('\n')[1:]

def parse(val, mapping):
    for x in mapping:
        dst, src, rng = map(int, x.split())
        if src <= val <= src+rng:
            val = dst+(val-src)
            break
    return val


def calc_loc(seed):
    val = int(seed)
    val = parse(val, seed_soil)
    val = parse(val, soil_fert)
    val = parse(val, fert_water)
    val = parse(val, water_light)
    val = parse(val, light_temp)
    val = parse(val, temp_humid)
    return parse(val, humid_loc)

def p1():
    p1 = []
    for seed in seeds:
        p1.append(calc_loc(seed))
    print(min(p1))

p2_seeds = []

x = 1
for n in seeds[::2]:
    p2_seeds.append([n, seeds[x]])
    x+=2

p1()

"""
p2 = []
for seed in p2_seeds:
    start, rng = int(seed[0]), int(seed[1])
    for x in range(start, start+rng):
        p2.append(calc_loc(x))


print(min(p2))
"""

def rev_parse(val, mapping):
    for x in mapping:
        dst, src, rng = map(int, x.split())
        if dst <= val <= dst+rng:
            val = src+(val-dst)
            return [True, val]
    return [False, val]

def rev_calc(seed):
    val = int(seed)
    if rev_parse(val, humid_loc)[0]: 
        val = rev_parse(val, humid_loc)[1]
    if rev_parse(val, temp_humid)[0]: 
        val = rev_parse(val, temp_humid)[1]
    if rev_parse(val, light_temp)[0]: 
        val = rev_parse(val, light_temp)[1]
    if rev_parse(val, water_light)[0]: 
        val = rev_parse(val, water_light)[1]
    if rev_parse(val, fert_water)[0]: 
        val = rev_parse(val, fert_water)[1]
    if rev_parse(val, soil_fert)[0]: 
        val = rev_parse(val, soil_fert)[1]
    if rev_parse(val, seed_soil)[0]: 
        return rev_parse(val, seed_soil)[1]
    return -1

loop = True
n = 51399200

while loop:
    val = rev_calc(n)
    if val > -1: 
        for  seed in p2_seeds:
            start, rng = int(seed[0]), int(seed[1])
            if start <= val <= start+rng:
                print(n)
                print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))
                exit()
    n+=1

print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - startTime)))
