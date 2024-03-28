import sys

input = sys.stdin.readline

word = list(input().strip())
bomb = list(input().strip())

key = bomb[-1]
bomb.reverse()

stack = []

for i in range(len(word)):
    stack.append(word[i])
    if word[i] == key and len(stack) >= len(bomb):
        temp = []
        for j in range(len(bomb)):
            temp.append(stack.pop())
        if temp == bomb:
            continue
        else:
            for j in range(len(temp), 0, -1):
                stack.append(temp[j-1])

if len(stack) == 0:
    print('FRULA')
else:
    for i in range(len(stack)):
        print(stack[i], end='')
