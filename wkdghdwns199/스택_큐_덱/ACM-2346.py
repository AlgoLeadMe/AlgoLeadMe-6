from collections import deque

n = int(input())
deq = deque(enumerate(map(int, input().split())))
answer = []

while deq:
    cnt, paper = deq.popleft()
    answer.append(cnt + 1)

    if paper > 0:
        deq.rotate(-(paper - 1))
    elif paper < 0:
        deq.rotate(-paper)

for balloon in answer :
    print(balloon, end=' ')