class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                maxCount = max(count, maxCount)
        
        return maxCount
        