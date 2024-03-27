import sys
from heapq import *
input = sys.stdin.readline

def dijkstra(graph, start):
    length = [float('inf') for _ in graph]
    length[start] = 0
    queue = []
    heappush(queue, [length[start], start])
    
    while queue:
        current_length, current_target = heappop(queue)

        if length[current_target] < current_length :
            continue
        
        for new_target, new_length in graph[current_target] :
            len = current_length + new_length
            if len < length[new_target]:
                length[new_target] = len
                heappush(queue, [len, new_target])
    return length

items = []
N,M,R = map(int, input().split())
T = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(R):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))
    
for item in range(1, len(graph)) :
    result = dijkstra(graph, item)
    get = 0
    for i in range(len(result)):
        if result[i] <= M :
            get += T[i-1]
    items.append(get)

print(max(items))
