class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        11
        11
        10
        10
        10
        01

        
        '''

        maxNum = max(nums)
        l = 0
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == maxNum:
                maxLen = max(i - l + 1, maxLen)
                continue
            else:
                l = i + 1
        
        return maxLen

        