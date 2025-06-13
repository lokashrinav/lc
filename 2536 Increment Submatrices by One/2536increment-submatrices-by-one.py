class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        '''

        1, 1, 0, 0
        1, 2, 1, -1
        0, 1, 1, 0
        0, -1, 0, 1

        1, 0, -1
        0, 1, 0
        -1, 0, 1



        A[i][j] += A[i - 1][j] + A[i][j - 1] - A[i - 1][j - 1]
        '''

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        final = [[0] * (n) for _ in range(n)]

        for y1, x1, y2, x2 in queries:
            dp[y1 + 1][x1 + 1] += 1
            dp[y1 + 1][x2 + 2] -= 1
            dp[y2 + 2][x1 + 1] -= 1
            dp[y2 + 2][x2 + 2] += 1
        
        print(dp)

        for y in range(1, len(dp) - 1):
            for x in range(1, len(dp) - 1):
                dp[y][x] += dp[y][x - 1] + dp[y - 1][x] - dp[y - 1][x - 1] 
                final[y - 1][x - 1] = dp[y][x]
        
        print(dp)
        
        return final



        