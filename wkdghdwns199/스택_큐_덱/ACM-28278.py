from collections import deque
import sys
N = int(sys.stdin.readline())
deq = deque([])
while N :
    N-=1
    n = list(map(int, sys.stdin.readline().split()))
    if len(n) > 1 : deq.appendleft(n[1])
    else :
        if (n[0] == 2) : 
            if (len(deq) == 0) : print(-1)
            else : print(deq.popleft())
        elif (n[0] == 3) : print(len(deq))
        elif (n[0] == 4) : print(1 if len(deq) == 0 else 0)
        elif (n[0] == 5) : print(deq[0] if len(deq) !=0 else -1)