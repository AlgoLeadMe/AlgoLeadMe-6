import sys
from heapq import *

input = sys.stdin.readline

def dijkstra(graph, start):
    distance = [float('inf') for _ in graph]
    distance[start] = 0
    queue = []
    heappush(queue, [distance[start], start])

    while queue:
        cur_dist, cur_dest = heappop(queue)

        if distance[cur_dest] < cur_dist:
            continue

        for new_dest, new_dist in graph[cur_dest]:
            dist = cur_dist + new_dist
            if dist < distance[new_dest]:
                distance[new_dest] = dist
                heappush(queue, [dist, new_dest])

    return distance


items = []
N, M, R = map(int, input().split())

item_weight = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(R):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))

for item in range(1, len(graph)):
    result = dijkstra(graph, item)
    can_get = 0
    for i in range(len(result)):
        if result[i] <= M:
            can_get += item_weight[i-1]
    items.append(can_get)

print(max(items))