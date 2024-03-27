import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

N,M,K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M) :
    x,y,z = map(int, input().split())
    trees[x-1][y-1].append(z)

ground = [[5] * N for _ in range(N)]
for _ in range(K) :
    
    for i in range(N) :
        for j in range(N):
            trees_length = len(trees[i][j])
            for k in range(trees_length) :
                if ground[i][j] >= trees[i][j][k] :
                    ground[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else :
                    for _ in range(k,trees_length):
                        ground[i][j] += trees[i][j].pop() // 2
                    break

    for i in range(N):
        for j in range(N) :
            for z in trees[i][j] :
                if z % 5 == 0:
                    for idx in range(8):
                        move_x = i + dx[idx]
                        move_y = j + dy[idx]
                        if 0 <= move_x < N and 0 <= move_y < N :
                            trees[move_x][move_y].appendleft(1)
            ground[i][j] += A[i][j]

answer = 0
for i in range(N) :
    for j in range(N):
        answer += len(trees[i][j])
print(answer)



