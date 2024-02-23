N = int(input())
stack = []
while N:
    N-=1
    n = int(input())
    if (n==0) : stack.pop()
    else : stack.append(n)
    

print(sum(stack))