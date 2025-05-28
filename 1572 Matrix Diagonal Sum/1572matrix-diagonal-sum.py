class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        '''
        1 + 1 -> 1
        2 + 2 -> 2
        3 + 3 -> 

        1 + 2 -> 2
        1 + 3 -> 

        '''


        sum1 = 0
        for i in range(len(mat)):
            sum1 += mat[i][i]
        
        for i in range(len(mat)):
            sum1 += mat[i][len(mat) - 1 - i]

        if len(mat) % 2:
            sum1 -= mat[len(mat) // 2][len(mat) // 2]
        
        return sum1
        