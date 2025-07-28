class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(ind, current_or):
            if ind == len(nums):
                return 1 if current_or == max_or else 0
            
            # Include + Exclude
            return dfs(ind + 1, current_or | nums[ind]) + dfs(ind + 1, current_or)
        
        return dfs(0, 0)