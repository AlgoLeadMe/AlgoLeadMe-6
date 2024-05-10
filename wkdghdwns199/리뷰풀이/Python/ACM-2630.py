white_color = 0 
blue_color = 0

def divide(start_x, end_x, start_y, end_y) :
    global white_color, blue_color
    checking_color = paper[start_x][start_y]
    sw=0
    for index_x in range(start_x, end_x):
        for index_y in range(start_y, end_y):
            if paper[index_x][index_y] != checking_color :
                sw=1
                break
        if sw==1 : break
    
    if sw==0 : 
        if checking_color == 1 :
            blue_color = blue_color +1
        else :
            white_color = white_color + 1
    else :
        divide(start_x, int((start_x + end_x)/2), start_y, int((start_y+end_y)/2))
        divide(start_x, int((start_x+end_x)/2), int((start_y+end_y)/2), end_y)
        divide(int((start_x+end_x)/2), end_x, start_y, int((start_y+ end_y)/2))
        divide(int((start_x+end_x)/2), end_x, int((start_y+end_y)/2), end_y)
    return 

        
import sys
input = sys.stdin.readline



N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
 
divide(0,N,0,N)


print(white_color)
print(blue_color)



