import time

startTime = time.time()

with open("inputs/inp05.txt") as fh:
    INPUT = fh.read().rstrip().split('\n\n')
    
seeds = INPUT[0].split(':')[1].split()
seed_soil = []
soil_fert = []
fert_water = []
water_light = []
light_temp = []
temp_humid = []
humid_loc = []

for x in INPUT[1].split('\n')[1:]:
    seed_soil.append(x.split())

for x in INPUT[2].split('\n')[1:]:
    soil_fert.append(x.split())

for x in INPUT[3].split('\n')[1:]:
    fert_water.append(x.split())

for x in INPUT[4].split('\n')[1:]:
    water_light.append(x.split())

for x in INPUT[5].split('\n')[1:]:
    light_temp.append(x.split())

for x in INPUT[6].split('\n')[1:]:
    temp_humid.append(x.split())

for x in INPUT[7].split('\n')[1:]:
    humid_loc.append(x.split())

def parse(mapping):
    for map in mapping:
        d = []
        dest = int(map[0])
        source = int(map[1])
        amt = int(map[2])
        for n, x in enumerate(range(source, source+amt+1)):
            d.append({'source':x, 'dest':dest+n})
        print(d)

parse(seed_soil)




"""    
print('Seeds:', seeds)
print('Seed-to-soil:', seed_soil)
print('Soil-fertiliser:', soil_fert)
print('Fertiliser-to-water:', fert_water)
print('Water-to-light:', water_light)
print('Light-to-temperature:', light_temp)
print('Temperature-to-humidity:', temp_humid)
print('Humidity-to-location:', humid_loc)
"""