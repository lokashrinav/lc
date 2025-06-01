class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        
        minNums = []
        maxNums = []

        for i in range(len(matrix)):
            minNum = float('inf')
            for p in range(len(matrix[0])):
                minNum = min(minNum, matrix[i][p])
            minNums.append(minNum)

        for p in range(len(matrix[0])):
            maxNum = float('-inf')
            for i in range(len(matrix)):
                maxNum = max(maxNum, matrix[i][p])
            maxNums.append(maxNum)
        
        res = []
        for i in range(len(matrix)):
            for p in range(len(matrix[0])):
                if matrix[i][p] == minNums[i] == maxNums[p]:
                    res.append(matrix[i][p])
        
        return res
