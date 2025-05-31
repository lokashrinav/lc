class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        res = [0, 0]

        for i in range(len(mat)):
            total = 0
            for p in range(len(mat[0])):
                total += mat[i][p]
            if total > res[1]:
                res = [i, total]
        
        return res