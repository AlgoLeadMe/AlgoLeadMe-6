import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    dp = [[0] * (M+1) for _ in range(N+1)]
    for x in range(1, N+1) :
        for y in range(1, M+1) :
            if x == 1 : dp[x][y] = y
            else : dp[x][y] = dp[x-1][y-1] + dp[x][y-1]
    
    print(dp[N][M])