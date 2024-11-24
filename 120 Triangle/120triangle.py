class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * (len(triangle) + 1) for _ in range(len(triangle) + 1)]

        for i in range(len(triangle) - 1, -1, -1):
            for p in range(len(triangle[i]) - 1, -1, -1):
                dp[i][p] = triangle[i][p] + min(dp[i + 1][p], dp[i + 1][p + 1])
        print(dp)
        return dp[0][0]




        

        