class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        '''

        values[0] - j

        '''

        res = []
        maxNum1 = float('-inf')
        for i in range(len(values) - 1, -1, -1):
            maxNum1 = max(maxNum1, values[i] - i)
            res.append(maxNum1)
        
        res = res[::-1]

        maxNum = float('-inf')
        for i in range(len(values) - 1):
            maxNum = max(maxNum, values[i] + i + res[i + 1])
        
        return maxNum
        