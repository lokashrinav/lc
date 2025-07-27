class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''

        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        ["1","0","1","0"],
        ["1","0","1","1"],
        ["1","0","1","1"],
        ["1","1","1","1"]

        '''

        dp = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]

        for y in range(1, len(matrix) + 1):
            for x in range(1, len(matrix[0]) + 1):
                if matrix[y - 1][x - 1] == "1":
                    dp[y][x] = min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + 1
        
        maxNum = 0
        for y in range(len(dp)):
            for x in range(len(dp[0])):
                maxNum = max(maxNum, dp[y][x] * dp[y][x])

        print(dp)
        
        return maxNum
        