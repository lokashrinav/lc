class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.hate = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            pref = 0
            for p in range(1, len(matrix[0]) + 1):
                pref += matrix[i - 1][p - 1]
                above = self.hate[i - 1][p]
                self.hate[i][p] = pref + above
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1 
        row2 += 1
        col2 += 1
        return self.hate[row2][col2] + self.hate[row1 - 1][col1 - 1] - self.hate[row2][col1 - 1] - self.hate[row1 - 1][col2]

    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)