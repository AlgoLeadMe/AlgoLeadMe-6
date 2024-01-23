n = int(input())
x = []
y = []

for i in range (0,n):  
    tempX,tempY = map(int, input().split())
    x.append(tempX)
    y.append(tempY)
     
x.sort()
y.sort()

print((x[n-1] - x[0]) * (y[n-1] - y[0]))