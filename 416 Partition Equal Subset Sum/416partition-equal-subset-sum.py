class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
            22 21
            0  1
        '''

        total = sum(nums)

        if total % 2 != 0:
            return False

        memo = {}
        total = sum(nums)
        def dfs(ind, sum1):
            # print(ind, sum1)
            if sum1 * 2 == total:
                return True
            if sum1 * 2 < total:
                return False
            if ind >= len(nums):
                return False
            if (ind, sum1) in memo:
                return memo[(ind, sum1)]
            
            memo[(ind, sum1)] = dfs(ind + 1, sum1) or dfs(ind + 1, sum1 - nums[ind])

            return memo[(ind, sum1)]
        
        return dfs(0, total)


        