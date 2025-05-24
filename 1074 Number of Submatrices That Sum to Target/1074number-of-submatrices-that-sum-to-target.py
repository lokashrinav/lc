class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        '''

        0, 0, 0, 0
        0, 0, 1, 1
        0, 1, 3, 4
        0, 1, 4, 5

        '''

        dp = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]

        for i in range(1, len(matrix) + 1):
            for p in range(1, len(matrix[0]) + 1):
                #print(len(matrix) + 1, len(matrix[0]) + 1, )
                dp[i][p] = matrix[i - 1][p - 1] + dp[i - 1][p] + dp[i][p - 1] - dp[i - 1][p - 1]

        print(dp)

        total = 0
        for i in range(1, len(dp)):
            for p in range(1, len(dp[0])):
                for w in range(i):
                    for v in range(p):
                        sum1 = dp[i][p] - dp[w][p] - dp[i][v] + dp[w][v]
                        if sum1 == target:
                            total += 1
        
        return total        