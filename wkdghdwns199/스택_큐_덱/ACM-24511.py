from collections import deque

# 데이터 받기
N = int(input())
queue_stack = list(map(int, input().split()))
data = list(map(int, input().split()))
n = int(input())
numbers = list(map(int, input().split()))

answer = deque()

for i in range(N) :
    if queue_stack[i] == 0:
        answer.append(data[i])

for number in numbers :
    answer.appendleft(number)


for _ in range(n) :
    print(answer.pop(), end=' ')