import sys
from collections import deque
input = sys.stdin.readline
deq = deque()
N = int(input())
for _ in range(N) :
    cmd = list(map(int, input().split()))
    if cmd[0] == 1 :
        deq.appendleft(cmd[1])
    elif cmd[0] == 2 :
        deq.append(cmd[1])
    elif cmd[0] == 3 :
        print(-1 if len(deq) == 0 else deq.popleft())
    elif cmd[0] == 4 :
        print(-1 if len(deq) == 0 else deq.pop())
    elif cmd[0] == 5 :
        print(len(deq))
    elif cmd[0] == 6 :
        print(1 if len(deq) == 0 else 0)
    elif cmd[0] == 7 :
        print(-1 if len(deq)==0 else deq[0])
    elif cmd[0] == 8:
        print(-1 if len(deq)==0 else deq[len(deq)-1])