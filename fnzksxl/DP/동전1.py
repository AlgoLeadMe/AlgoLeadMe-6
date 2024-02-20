import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
dp = [0 for _ in range(K+1)]
dp[0] = 1

for _ in range(N):
  coin.append(int(input()))

for i in coin:
  for j in range(i, K+1):
    if j-i >= 0:
      dp[j] += dp[j-i]
      
print(dp[K])