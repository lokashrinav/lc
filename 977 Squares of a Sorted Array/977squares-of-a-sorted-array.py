class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:


        l, r = 0, len(nums) - 1
        res = []

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l])
                l += 1
            else:
                res.append(nums[r])
                r -= 1 
        
        for i in range(len(res)):
            res[i] **= 2
        
        res.reverse()

        return res
        
        