class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        count = 0

        while count < n * n:
            for i in range(left, right + 1):
                count += 1
                matrix[top][i] = count
            top += 1

            for i in range(top, bottom + 1):
                count += 1
                matrix[i][right] = count
            right -= 1

            for i in range(right, left - 1, -1):
                count += 1
                matrix[bottom][i] = count
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                count += 1
                matrix[i][left] = count
            left += 1
        
        return matrix

                
