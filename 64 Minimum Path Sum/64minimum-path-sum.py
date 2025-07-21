class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        '''

        dp[i][j] = dp[i][j] + min(dp[i + 1][j], dp[i][j + 1])

        '''

        dp = grid
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i + 1 < len(grid) and j + 1 < len(grid[0]):
                    dp[i][j] += min(dp[i + 1][j], dp[i][j + 1])
                elif i + 1 < len(grid):
                    dp[i][j] += dp[i + 1][j]
                elif j + 1 < len(grid[0]):
                    dp[i][j] += dp[i][j + 1]
        
        return dp[0][0]
        