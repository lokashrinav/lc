class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = [[None for i in range(len(matrix[0]))] for p in range(len(matrix))]

        def dfs(index, prevNum, prevIndex):
            y, x = index
            if not (y >= 0 and x >= 0 and y < len(matrix) and x < len(matrix[0])):
                return 0

            currNum = matrix[y][x]

            if prevNum >= currNum:
                return 0

            if dp[y][x]:
                return dp[y][x]

            total = float('-inf')
            if prevIndex != (y + 1, x):
                total = max(dfs((y + 1, x), currNum, index) + 1, total)
            if prevIndex != (y - 1, x):
                total = max(dfs((y - 1, x), currNum, index) + 1, total)
            if prevIndex != (y, x + 1):
                total = max(dfs((y, x + 1), currNum, index) + 1, total)
            if prevIndex != (y, x - 1):
                total = max(dfs((y, x - 1), currNum, index) + 1, total)

            dp[y][x] = total

            return dp[y][x]

        maxNum = float('-inf')

        for i in range(len(matrix)):
            for p in range(len(matrix[0])):
                if not dp[i][p]:
                    dp[i][p] = dfs((i, p), -1, (-1, -1))

        print(dp)

        for i in range(len(matrix)):
            for p in range(len(matrix[0])):
                maxNum = max(dp[i][p], maxNum)

        return maxNum

