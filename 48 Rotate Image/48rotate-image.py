class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        0, 1
        1, 2
        """
        
        for y in range(len(matrix)):
            for x in range(y + 1, len(matrix[0])):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
        
        for y in range(len(matrix)):
            for x in range(len(matrix[0]) // 2):
                matrix[y][len(matrix[0]) - x - 1], matrix[y][x] = matrix[y][x], matrix[y][len(matrix[0]) - x - 1]
        
        return matrix
