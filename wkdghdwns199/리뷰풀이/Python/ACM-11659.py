import sys
input = sys.stdin.readline
N,M = map(int, input().split())
num_list = list(map(int, input().split()))
accumulate_list = [0] * (N+1)
for i in range(N):
    accumulate_list[i+1] = accumulate_list[i] + num_list[i]

for _ in range(M):
    start, end = map(int, input().split())
    print(accumulate_list[end] - accumulate_list[start-1])