class Solution:
    def maxFreqSum(self, s: str) -> int:
        hmap = Counter(s)
        maxNum = 0
        maxNum2 = 0

        for key, val in hmap.items():
            if key in 'aeiou':
                maxNum = max(maxNum, val)
            else:
                maxNum2 = max(maxNum2, val)
            
        return maxNum + maxNum2
        