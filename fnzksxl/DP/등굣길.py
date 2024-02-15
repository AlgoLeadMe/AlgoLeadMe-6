def solution(m, n, puddles):
    dp = [[0 for i_ in range(m+1)] for j in range(n+1)]
    
    dp[0][1] = 1
    
    for puddle in puddles:
        a,b = puddle
        dp[b][a] = -1
    
    for j in range(1,m+1):
        for i in range(1,n+1):
            if dp[i][j] == -1:
                continue
            elif dp[i-1][j] == -1:
                dp[i][j] = dp[i][j-1]
            elif dp[i][j-1] == -1:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])
                
    return dp[n][m]%1000000007