from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
queue = deque()
_map = []
visited = [[False] * M for _ in range(N)]
result = [[-1]*M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 2 :
            queue.append((i,j))
            visited[i][j] = True
            result[i][j] = 0
        if row[j] == 0 :
            result[i][j] = 0
    _map.append(row)

direction = [(1,0), (-1,0), (0,1), (0,-1)]
while queue :
    x,y = queue.popleft()
    for dx, dy in direction :
        move_x, move_y = x+dx, y+dy
        if 0<=move_x < N and 0<=move_y < M and visited[move_x][move_y] == False and _map[move_x][move_y] :
            queue.append((move_x, move_y))
            visited[move_x][move_y] = True
            result[move_x][move_y] = result[x][y] + 1

for row in result :
    for i in row :
        print (i, end=' ')
    print()