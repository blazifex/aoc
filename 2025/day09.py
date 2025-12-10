import time
from shapely.geometry import Point, Polygon

start_time = time.time()
p1, p2 = 0, 0

with open("inputs/inp09.txt") as fh:
    input = fh.read().strip().split('\n')

for r, row in enumerate(input):
    input[r] = [int(x) for x in row.split(',')]

all_areas = []
bounded_areas = []
bounds = Polygon(input)

for i, row in enumerate(input):
    for j in range(i+1, len(input)):
        min_x, max_x = sorted([row[0], input[j][0]])
        min_y, max_y = sorted([row[1], input[j][1]])

        width = max_x - min_x + 1
        height = max_y - min_y + 1
        area = width * height
        all_areas.append(area)
        
        shape = Polygon([(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)])
        if shape.within(bounds): bounded_areas.append(area)

p1 = max(all_areas)
p2 = max(bounded_areas)

print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))