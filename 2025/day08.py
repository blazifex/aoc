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

pairs.sort(key=lambda x: x["distance"])

def make_circuits(pairs):
    circuits = []
    final_a = None
    final_b = None

    for p, pair in enumerate(pairs):
        a_circuit = None
        b_circuit = None
        for circuit in circuits:
                if pair["a"] in circuit: a_circuit = circuit
                if pair["b"] in circuit: b_circuit = circuit
        if a_circuit and b_circuit:
            if a_circuit != b_circuit:
                a_circuit += [x for x in b_circuit if x not in a_circuit]
                circuits.remove(b_circuit)
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
            circuits.append([pair["a"], pair["b"]])
        
    
    return circuits, final_a, final_b

p1_circuits = make_circuits(pairs[:1000])[0]

p1_circuits.sort(key=len, reverse=True)

for circuit in p1_circuits[:3]:
    p1 *= len(circuit)

final_a, final_b = make_circuits(pairs)[1:]

p2 = final_a[0] * final_b[0]

print("P1: ", p1)
print("P2: ", p2)
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))