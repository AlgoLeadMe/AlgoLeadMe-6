import sys
from heapq import *

input=sys.stdin.readline

vertex, edge = map(int, input().split())
start_vertex = int(input())
graph = {v : [] for v in range(1,vertex+1)}
for _ in range(edge) :
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

heap = []
result = [int(1e9)] * (vertex+1)
result[start_vertex] = 0
heappush(heap, (start_vertex,0))

while heap :

    current_node, current_weight = heappop(heap)
    if result[current_node] < current_weight :
        continue
    for node, weight in graph[current_node]:
        distance = current_weight + weight
        if distance < result[node]:
            result[node] = distance
            heappush(heap, (node, distance))

for i in range(1,vertex+1):
    if result[i] == int(1e9):
        print('INF')
    else :
        print(result[i])


