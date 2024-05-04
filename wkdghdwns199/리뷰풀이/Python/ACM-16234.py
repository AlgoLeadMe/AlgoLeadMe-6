import sys
from collections import deque
input = sys.stdin.readline
N,L,R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
q = deque()
#연합이 될 수 있을지 확인 후 연랍이 되면 저장
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q.append((x,y))
    union=[]
    union.append((x,y))
    while q:
        a,b = q.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if na >= N or nb>= N or nb<0 or na <0 or visited[na][nb]==1:
                continue
            if R>=abs(country[a][b]-country[na][nb]) >= L:
                visited[na][nb] = 1
                q.append((na,nb))
                union.append((na,nb))
    if len(union)<=1:
        return 0
    result=sum(country[a][b] for a,b in union) // len(union)
    for a,b in union:
        country[a][b] = result

    return 1
day=0

while True :
    stop = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                stop += bfs(i,j)
    if stop ==0:
        break
    day+=1
print(day)