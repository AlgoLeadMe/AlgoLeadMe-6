import sys
import math 

array = [True for i in range (1000001)]    

for i in range (2,1001) :
    if array[i] :
        for k in range (i*2, 1000001, i):
            array[k] = False

T = int(sys.stdin.readline().strip())
while T > 0:
    T -=1
    count = 0
    N = int(sys.stdin.readline().strip())
    for x in range(2, N//2+1) :
        if array[x] and array[N-x]:
            count+=1

    print(count)