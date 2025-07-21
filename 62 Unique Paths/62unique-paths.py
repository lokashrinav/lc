class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * (n + 1) for i in range(m + 1)]

        '''

        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        '''

        dp[1][1] = 1

        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] += dp[i][j + 1] + dp[i + 1][j]
        
        return dp[-1][-1]
        