import time

start_time = time.time()
p1, p2 = 0, 0

with open("inputs/inp05.txt") as fh:
    input = fh.read().strip().split('\n\n')

id_sets = [list(map(int, line.split('-'))) for line in input[0].split('\n')]
ingredients = input[1].split('\n')

for ingredient in ingredients:
    spoiled = True
    for id_set in id_sets:
        if int(ingredient) >= int(id_set[0]) and int(ingredient) <= int(id_set[1]) and spoiled: 
            spoiled = False
    if not spoiled: p1 += 1

fresh_ids = []
id_sets.sort(key=lambda x: x[0])

for id_set in id_sets:
    integrated = False
    for n, fresh_id in enumerate(fresh_ids):
        if id_set[0] <= fresh_id[1]+1 and not integrated:
            fresh_ids[n][1] = max(fresh_id[1], id_set[1])
            integrated = True
    if not integrated: fresh_ids.append(id_set)

for fresh_id in fresh_ids:
    p2 += int(fresh_id[1]) - int(fresh_id[0]) + 1

print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))