class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * (len(obstacleGrid[0]) + 1) for i in range(len(obstacleGrid) + 1)]

        for i in range(len(obstacleGrid) - 1, -1, -1):
            for p in range(len(obstacleGrid[0]) - 1, -1, -1):
                if obstacleGrid[i][p] == 1:
                    dp[i][p] = 0
                elif p == len(obstacleGrid[0]) - 1 and i == len(obstacleGrid) - 1:
                    dp[i][p] = 1
                else:
                    dp[i][p] = dp[i + 1][p] + dp[i][p + 1]
        print(dp)
        return dp[0][0]

        