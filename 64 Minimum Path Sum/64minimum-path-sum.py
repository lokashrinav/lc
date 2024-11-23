class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(len(grid[0]) + 1)] for p in range(len(grid) + 1)]

        for i in range(len(grid) - 1, -1, -1):
            for p in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and len(grid[0]) - 1 == p:
                    dp[i][p] = grid[i][p]
                else:
                    dp[i][p] = min(dp[i + 1][p], dp[i][p + 1]) + grid[i][p]

        print(dp)
        
        return dp[0][0]
            