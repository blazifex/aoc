import time, math

start_time = time.time()
p1, p2 = 1, 0

with open("inputs/inp08.txt") as fh:
    input = fh.read().strip().split('\n')

junctions = []

for r, row in enumerate(input):
    junctions.append([int(x) for x in row.split(',')])

def calc_distance(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)

pairs = []

for x in range(len(junctions)-1):
    for y in range(x+1, len(junctions)):    
        pairs.append({
            "a": tuple(junctions[x]),
            "b": tuple(junctions[y]),
            "distance": calc_distance(junctions[x], junctions[y])
            })

#sort pairs by minimum distance
pairs.sort(key=lambda x: x["distance"])

circuits = [[pairs[0]["a"], pairs[0]["b"]]]
x = 0

for pair in pairs[1:1000]:
    a_circuit = None
    b_circuit = None
    for circuit in circuits:
            if pair["a"] in circuit: a_circuit = circuit
            if pair["b"] in circuit: b_circuit = circuit

    if a_circuit and b_circuit:
        if a_circuit != b_circuit:
            # merge b_circuit into a_circuit
            a_circuit += [x for x in b_circuit if x not in a_circuit]
            circuits.remove(b_circuit)
    elif a_circuit:
        if pair["b"] not in a_circuit:
            a_circuit.append(pair["b"])
    elif b_circuit:
        if pair["a"] not in b_circuit:
            b_circuit.append(pair["a"])
    else:
        circuits.append([pair["a"], pair["b"]])

circuits.sort(key=len, reverse=True)
for circuit in circuits[:3]:
    p1 *= len(circuit)


circuits2 = [[pairs[0]["a"], pairs[0]["b"]]]
final_a = None
final_b = None

for pair in pairs:
    a_circuit = None
    b_circuit = None
    for circuit in circuits2:
            if pair["a"] in circuit: a_circuit = circuit
            if pair["b"] in circuit: b_circuit = circuit

    if a_circuit and b_circuit:
        if a_circuit != b_circuit:
            # merge b_circuit into a_circuit
            a_circuit += [x for x in b_circuit if x not in a_circuit]
            circuits2.remove(b_circuit)
    elif a_circuit:
        if pair["b"] not in a_circuit:
            a_circuit.append(pair["b"])
            final_a = pair["a"]
            final_b = pair["b"]
    elif b_circuit:
        if pair["a"] not in b_circuit:
            b_circuit.append(pair["a"])
            final_a = pair["a"]
            final_b = pair["b"]
    else:
        circuits2.append([pair["a"], pair["b"]])

p2 = final_a[0] * final_b[0]

print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))