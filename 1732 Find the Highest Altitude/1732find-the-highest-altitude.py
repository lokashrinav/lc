class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        start = 0
        maxNum = 0
        for i in range(len(gain)):
            start += gain[i]
            maxNum = max(start, maxNum)
        
        return maxNum
        


        