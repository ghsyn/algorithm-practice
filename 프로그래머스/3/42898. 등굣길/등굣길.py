def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if x == 1 and y == 1:
                dp[x][y] = 1
                continue
            if [y, x] in puddles:
                dp[x][y] = 0
                continue
            dp[x][y] = (dp[x - 1][y] + dp[x][y - 1])  % 1000000007
    return dp[n][m]