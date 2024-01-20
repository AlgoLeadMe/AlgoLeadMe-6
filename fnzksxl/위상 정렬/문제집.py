import sys
import heapq

input = sys.stdin.readline

N, m = map(int, input().split())
degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
heap = []

for _ in range(m):
    first, later = map(int, input().split())
    degree[later] += 1
    graph[first].append(later)

for i in range(1, N+1):
    if not degree[i]:
        heapq.heappush(heap, i)

        
while heap:
    cur = heapq.heappop(heap)
    print(cur, end=" ")
    
    for node in graph[cur]:
        degree[node] -= 1
        if not degree[node]:
            heapq.heappush(heap, node)