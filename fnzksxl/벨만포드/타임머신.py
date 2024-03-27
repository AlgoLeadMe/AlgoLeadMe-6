import sys

input = sys.stdin.readline


def func():
    distances[1] = 0

    for i in range(N):
        for j in range(M):
            cur_node, next_node, weight = edges[j]
            if distances[cur_node] != float('inf') and distances[next_node] > distances[cur_node] + weight:
                distances[next_node] = distances[cur_node] + weight
                if i == N-1:
                    return False

    return True


N, M = map(int, input().split())

edges = []
distances = [float('inf')] * (N+1)
q = []

for _ in range(M):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))


if func():
    for weight in distances[2:]:
        if weight == float('inf'):
            print(-1)
        else:
            print(weight)
else:
    print(-1)
