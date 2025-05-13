class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        for i in range(len(mat)):
            y, x = i, 0
            res = []
            while y < len(mat) and x < len(mat[0]):
                res.append(mat[y][x])
                y += 1
                x += 1
            
            res.sort()

            y, x = i, 0
            while y < len(mat) and x < len(mat[0]):
                mat[y][x] = res[x]
                y += 1
                x += 1

        for i in range(len(mat[0])):
            y, x = 0, i
            res = []
            while y < len(mat) and x < len(mat[0]):
                res.append(mat[y][x])
                y += 1
                x += 1
            
            res.sort()

            y, x = 0, i
            while y < len(mat) and x < len(mat[0]):
                mat[y][x] = res[y]
                y += 1
                x += 1
        
        return mat
        