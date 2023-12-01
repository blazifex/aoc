import os, time
import numpy as np
import heapq

def main(input: list):
    p1 = np.array(input)

    p2 = np.concatenate([p1+x for x in range(5)], 0)
    p2 = np.concatenate([p2+x for x in range(5)], 1)
    p2 = np.where(p2 > 9, p2-9, p2)

    p1_neighbours = get_neighbours(p1)
    p2_neighbours = get_neighbours(p2)

    print("Part 1:", run(p1, p1_neighbours))
    print("Part 2:", run(p2, p2_neighbours))

def get_neighbours(i: list):
    graph = {}
    for r in range(len(i)):
        for c in range(len(i[0])):
            next_points = []
            if r > 0: next_points.append([r-1, c])
            if r < len(i)-1: next_points.append([r+1, c])
            if c > 0: next_points.append([r, c-1])
            if c < len(i[0])-1: next_points.append([r, c+1])
            graph[r, c] = next_points
        
    return graph

def run(i: list, graph: dict):
    goal = [len(i)-1, (len(i[0])-1)]
    dist = {}
    stack = []

    for r in range(len(i)):
        for c in range(len(i[0])):
            dist[r,c] = float('inf')

    heapq.heappush(stack, (0, [0,0]))

    while len(stack) > 0:
        cur = heapq.heappop(stack)

        for neighbour in graph[tuple(cur[1])]:
            tmp = cur[0] + i[tuple(neighbour)]
            if tmp < dist[tuple(neighbour)]:
                dist[tuple(neighbour)] = tmp
                heapq.heappush(stack, (tmp, tuple(neighbour)))
    
    return dist[tuple(goal)]

if __name__ == "__main__": 
    start_time = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+"/inputs/inp15.txt","r") as f:
        input = [[int(char) for char in line] for line in f.read().split('\n')]
    main(input)
    print ('[Finished in {:.3f}s]'.format((time.time() - start_time)))