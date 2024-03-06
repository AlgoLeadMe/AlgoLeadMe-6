import sys
from collections import deque
input = sys.stdin.readline

N, K= map(int, input().split())
circle_list = deque([number for number in range(1,N+1)])
print('<', end='')
while circle_list :
    circle_list.rotate(-(K-1))
    print(circle_list.popleft(), end='')
    if len(circle_list) != 0 : print(', ', end='')
print('>')