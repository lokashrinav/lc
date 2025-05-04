class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        '''

        4
        
        3, 2, 1, 

        '''

        memo = {}
        def dfs(target):
            if target == 0:
                return 1
            
            if target < 0:
                return 0
            
            if target in memo:
                return memo[target]
            
            total = 0
            for i in range(len(nums)):
                total += dfs(target - nums[i])
            
            memo[target] = total
            
            return total
        
        return dfs(target)