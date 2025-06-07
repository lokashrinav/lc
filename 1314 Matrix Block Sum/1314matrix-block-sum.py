class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        dp = [[0] * (len(mat[0]) + 1) for i in range(len(mat) + 1)]

        answer = [[0] * (len(mat[0])) for i in range(len(mat))]

        for i in range(1, len(mat) + 1):
            for p in range(1, len(mat[0]) + 1):
                dp[i][p] = mat[i - 1][p - 1] + dp[i][p - 1] + dp[i - 1][p] - dp[i - 1][p - 1]
        
        print(dp)

        def query(r2, c2, r1, c1):
            return dp[r2][c2] - dp[r1][c2] - dp[r2][c1] + dp[r1][c1]
        
        for y in range(len(answer)):
            for x in range(len(answer[0])):
                answer[y][x] = query(min(y + k + 1, len(dp) - 1), min(x + k + 1, len(dp[0]) - 1), max(y - k, 0), max(x - k, 0))
        
        return answer

        