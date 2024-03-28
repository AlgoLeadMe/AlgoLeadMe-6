import sys
input = sys.stdin.readline

def fib(n) :
    global countFib
    if n==1 or n==2:
        countFib += 1
        return 1
    else :
        return fib(n-1) + fib(n-2)

def fibo(n):
    global countFibo
    f = [0 for _ in range(n+1)]
    f[1] = f[2] = 1
    for idx in range(3, n+1):
        countFibo+=1
        f[idx] = f[idx-1] + f[idx-2]
    return f[n]

N = int(input())
countFib = countFibo = 0
fib(N)
fibo(N)
print(countFib, countFibo)