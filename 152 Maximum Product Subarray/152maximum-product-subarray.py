class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        prod1 = 1
        prod2 = 1
        res = []
        result = nums[0]
        for i in range(len(nums)):
            newMax = max(nums[i], prod1 * nums[i], prod2 * nums[i])
            newMin = min(nums[i], prod1 * nums[i], prod2 * nums[i])
            prod1 = newMax
            prod2 = newMin
            result = max(result, prod1)
            res.append(result)
        
        return max(res)
        
        
        






        