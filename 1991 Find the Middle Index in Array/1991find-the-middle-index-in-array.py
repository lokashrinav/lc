class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        sum1 = 0
        sum2 = sum(nums)
        for i in range(len(nums)):
            sum2 -= nums[i]
            if sum1 == sum2:
                return i
            sum1 += nums[i]
        
        return -1