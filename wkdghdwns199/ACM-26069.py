import sys
input = sys.stdin.readline
N = int(input())
dancingCheck = {}
dancingCheck['ChongChong'] = True
for _ in range(N):
    left_rabbit, right_rabbit = map(str, input().split())
    try :
        if dancingCheck[left_rabbit]:
            dancingCheck[right_rabbit] = True
    except :
        dancingCheck[left_rabbit] = False
        
    try :
        if dancingCheck[right_rabbit] :
            dancingCheck[left_rabbit] = True
    except :
        dancingCheck[right_rabbit] = False

count=0
for key in dancingCheck.keys():
    if dancingCheck[key] == True:
        count+=1
    
print(count)