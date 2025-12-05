import time

start_time = time.time()
p1, p2 = 0, 0

with open("inputs/inp05.txt") as fh:
    input = fh.read().strip().split('\n\n')

fresh_ranges = [list(map(int, line.split('-'))) for line in input[0].split('\n')]
ingredient_ids = list(map(int, input[1].split('\n')))

for ingredient_id in ingredient_ids:
    spoiled = True
    for fresh_range in fresh_ranges:
        if ingredient_id >= fresh_range[0] and ingredient_id <= fresh_range[1] and spoiled: 
            spoiled = False
    if not spoiled: p1 += 1

merged_ranges = []
fresh_ranges.sort(key=lambda x: x[0])

for fresh_range in fresh_ranges:
    integrated = False
    for n, merged_range in enumerate(merged_ranges):
        if fresh_range[0] <= merged_range[1]+1 and not integrated:
            merged_ranges[n][1] = max(merged_range[1], fresh_range[1])
            integrated = True
    if not integrated: merged_ranges.append(fresh_range)

for merged_range in merged_ranges:
    p2 += int(merged_range[1]) - int(merged_range[0]) + 1

print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))