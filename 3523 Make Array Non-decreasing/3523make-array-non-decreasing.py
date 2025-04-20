class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prev = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] >= prev:
                count += 1
                prev = nums[i]
        return count
                
                
            
        