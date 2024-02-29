import sys
from collections import deque
N = int(input())
queue = deque()
for _ in range(N):
    _str = sys.stdin.readline().split()
    if 'push' == _str[0] :
        queue.append(_str[1])
    elif 'pop' == _str[0] :
        if len(queue) == 0 : print(-1)
        else : print(queue.popleft())
    elif 'size' == _str[0] :
        print(len(queue))
    elif 'empty' == _str[0] :
        if len(queue) == 0 : print(1)
        else : print(0)
    elif 'front' == _str[0] :
        if len(queue) == 0 : print(-1)
        else : print(queue[0])
    elif 'back' == _str[0] :
        if len(queue) == 0 : print(-1)
        else : print(queue[len(queue)-1])
        