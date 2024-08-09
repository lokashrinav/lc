class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for y in range(len(matrix)):
            for x in range(y, len(matrix[0])):
                tmp = matrix[y][x]
                matrix[y][x] = matrix[x][y]
                matrix[x][y] = tmp
                
        for row in matrix:
            row.reverse()

        
        