class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''

        dp[i][j] += min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        '''
        
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                minNum = float('inf')
                if i - 1 >= 0 and j - 1 >= 0:
                    minNum = matrix[i - 1][j - 1]
                if i - 1 >= 0:
                    minNum = min(minNum, matrix[i - 1][j])
                if i - 1 >= 0 and j + 1 < len(matrix[0]):
                    minNum = min(minNum, matrix[i - 1][j + 1])
                    
                matrix[i][j] += minNum
        
        #print(matrix)

        return min(matrix[-1])