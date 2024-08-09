class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix[0])
        width = len(matrix)
        visited = set()
        for y in range(width):
            for x in range(length):
                if matrix[y][x] == 0:
                    for z in range(length):
                        if matrix[y][z] != 0:
                            matrix[y][z] = None
                    for z in range(width):
                        if matrix[z][x] != 0:
                            matrix[z][x] = None
        for y in range(width):
            for x in range(length):
                if matrix[y][x] == None:
                    matrix[y][x] = 0
        