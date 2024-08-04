class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Grab val of Current Left and val of current Right
        # 
        maxVal = nums[0]
        val = 0
        for i in range(len(nums)):
            if val < 0:
                val = 0
            val += nums[i]
            
            maxVal = max(val, maxVal)
        return maxVal
            
            
        
        
        
        