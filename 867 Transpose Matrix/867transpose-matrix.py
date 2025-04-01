class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        newMatrix = [[0 for i in range(len(matrix))] for p in range(len(matrix[0]))]

        for i in range(len(matrix[0])):
            for p in range(len(matrix)):
                newMatrix[i][p] = matrix[p][i]
        
        return newMatrix
        