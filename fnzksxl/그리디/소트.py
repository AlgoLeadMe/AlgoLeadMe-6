import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
S = int(input())

for i in range(N-1):
    if S==0:
        break
    _max = max(lst[i:i+S+1])
    idx = lst.index(_max)
    for j in range(idx, i, -1):
        lst[j], lst[j-1] = lst[j-1], lst[j]
        S -= 1

print(*lst)