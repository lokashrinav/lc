class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        

        # 5
        # 
        maxSum = 0
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            maxSum = max(sum1, maxSum)
            if sum1 < 0:
                sum1 = 0
            
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            maxSum = max(abs(sum1), maxSum)
            if sum1 > 0:
                sum1 = 0
        
        return maxSum

