class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        def checkDiag(y, x):
            prev = None
            while y < n and x < m:
                print(y, x)
                if prev is None:
                    prev = matrix[y][x]
                    y += 1
                    x += 1
                elif matrix[y][x] != prev:
                    return False
                else:
                    y += 1
                    x += 1
            print("")
            return True
                    

        for i in range(n):
            if not checkDiag(i, 0): 
                return False
    
        for i in range(m):
            if not checkDiag(0, i):
                return False
        
        return True
