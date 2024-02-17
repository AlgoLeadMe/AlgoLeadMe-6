from heapq import heappush, heappop

import sys

def dijkstra():
  q = []
  heappush(q, (startPoint, 0))
  distances[startPoint] = 0
  ways[startPoint].append(startPoint)
  
  while q:
    cur_dest, cur_dist = heappop(q)

    if distances[cur_dest]<cur_dist:
      continue
    
    for next_dest, next_dist in graph[cur_dest]:
      cost = distances[cur_dest] + next_dist
      
      if cost < distances[next_dest]:
        distances[next_dest] = cost
        ways[next_dest] = ways[cur_dest] + [next_dest]
        heappush(q, (next_dest,cost))  

  return distances[endPoint], len(ways[endPoint]), ways[endPoint]

input = sys.stdin.readline

INF = float('inf')
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distances = [INF] * (N+1)
ways=[[] for _ in range(N+1)]

for _ in range(M):
  start, end, weight = map(int, input().split())
  graph[start].append((end, weight))
  
startPoint, endPoint = map(int, input().split())

cost, length, way = dijkstra()

print(cost)
print(length)
print(*way)
