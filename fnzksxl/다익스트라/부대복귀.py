from heapq import heappop, heappush

def solution(n, roads, sources, destination):
    answer = []
    graph=[[] for _ in range(n+1)]
    
    for start, dest in roads:
        graph[start].append(dest)
        graph[dest].append(start)
    
    INF = 500001
    distances = [INF] * (n+1)
    distances[destination] = 0
    
    queue = []
    
    heappush(queue, (distances[destination], destination))
    
    while queue:
        cur_dist, cur_dest = heappop(queue)

        if distances[cur_dest] < cur_dist:
            continue

        for next_dest in graph[cur_dest]:
            distance = cur_dist + 1
            if distance < distances[next_dest]:
                distances[next_dest] = distance
                heappush(queue, (distance, next_dest))
            
    return [-1 if distances[s] == INF else distances[s] for s in sources]