from collections import deque
import sys
input = sys.stdin.readline



def waterMelt() :
    while waterPos :
        y,x = waterPos.popleft()
        maps[y][x] = '.'

        for dy,dx in dir :
            ny,nx = y+dy, x+dx
            if 0<=ny < r and 0 <= nx <c and not waterCheck[ny][nx] :
                if maps[ny][nx] == '.' :
                    waterPos.append((ny,nx))
                elif maps[ny][nx] == 'X' :
                    nextWaterPos.append((ny,nx))
                waterCheck[ny][nx] = True

def findSwan() :
    while swanPos :
        y,x = swanPos.popleft()

        if y == endY and x == endX :
            return True
    

        for dy,dx in dir :
            ny,nx = y + dy, x + dx
            if 0<= ny < r and 0 <= nx < c and not swanCheck[ny][nx] :
                if maps[ny][nx] == '.':
                    swanPos.append((ny,nx))
                elif maps[ny][nx] == 'X' :
                    nextSwanPos.append((ny,nx))
                swanCheck[ny][nx] = True
    return False


r,c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]
swanCheck = [[False] * c for _ in range(r)]
waterCheck = [[False] * c for _ in range(r)]
dir = [[1,0], [-1,0], [0,1], [0,-1]]

swanPos = deque()
nextSwanPos = deque()
waterPos = deque()
nextWaterPos = deque()


for i in range(r):
    for j in range(c):
        if maps[i][j] =='L' :
            if not swanPos :
                swanPos.append((i,j))
                swanCheck[i][j] = True
            else :
                endY, endX = i,j
            maps[i][j] = '.'

            waterPos.append((i,j))
            waterCheck[i][j] = True
        elif maps[i][j] == '.':
            waterPos.append((i,j))
            waterCheck[i][j] = True


days =0
while True :
    waterMelt()
    if findSwan() : break

    swanPos = nextSwanPos
    waterPos = nextWaterPos
    nextSwanPos = deque()
    nextWaterPos = deque()

    days+=1

print(days)

