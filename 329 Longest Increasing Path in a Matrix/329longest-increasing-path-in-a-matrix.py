class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        (2, 1) = 1 -> [2, 6]
        (2, 2) = 1 -> [8]
        (2, 0) = 2 -> [6]
        (1, 0) = 6 -> [9]
        '''

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(out):
            y, x = out
            if out in dp:
                return dp[out]
            
            curr = 0
            for ny, nx in dirs:
                dy, dx = y + ny, x + nx
                if len(matrix) > dy >= 0 and len(matrix[0]) > dx >= 0 and matrix[dy][dx] > matrix[y][x]:
                    curr = max(curr, dfs((dy, dx)))

            dp[(y, x)] = curr + 1
            return dp[(y, x)]
        
        maxNum = 0
        dp = {}
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                maxNum = max(maxNum, dfs((y, x)))
        
        return maxNum
                

        