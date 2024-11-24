class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if len(matrix) == 1:
            is_one = False
            for i in range(len(matrix[0])):
                if matrix[0][i] == "1":
                    is_one = True
            if is_one:
                return 1
            return 0
        
        if len(matrix[0]) == 1:
            is_one = False
            for i in range(len(matrix)):
                if matrix[i][0] == "1":
                    is_one = True
            if is_one:
                return 1
            return 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix[0])):
            dp[-1][i] = int(matrix[-1][i])
        
        for i in range(len(matrix)):
            dp[i][-1] = int(matrix[i][-1])

        for i in range(len(matrix) - 2, -1, -1):
            for p in range(len(matrix[0]) - 2, -1, -1):
                if matrix[i][p] == "0":
                    dp[i][p] = 0
                else:
                    dp[i][p] = 1 + min(int(dp[i + 1][p + 1]), int(dp[i + 1][p]), int(dp[i][p + 1]))

        print(dp)

        return max(max(x) for x in dp) ** 2

        