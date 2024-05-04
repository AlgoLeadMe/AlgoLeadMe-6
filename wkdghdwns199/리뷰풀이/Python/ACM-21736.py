from collections import deque
n,m = map(int, input().split())

direction_x = [-1, 1, 0, 0]
direction_y = [0, 0, -1, 1]

people_map = [ list(input()) for _ in range (n)]


deq = deque()
breakCheck = 0
for i in range (n) :
    for j in range(m):
        if people_map[i][j] == 'I' : 
            deq.append([i,j])
            breakCheck = 1
            break
    if breakCheck : break

answer = 0 
while deq :
    current_point = deq.pop()
    if people_map[current_point[0]][current_point[1]] == 'P':
        answer+=1
    people_map[current_point[0]][current_point[1]] = 'X'

    for i in range(4) :
        move_x = current_point[0] + direction_x[i]
        move_y = current_point[1] + direction_y[i]

        if n > move_x and move_x >= 0 and m > move_y and move_y  >= 0 :
            if people_map[move_x][move_y] != 'X' :
                deq.append([move_x, move_y])
    
if answer == 0 : print('TT')
else : print(answer)