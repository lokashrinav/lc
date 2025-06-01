class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:

        '''

        3 * 1 * 6 * 8 * 4 = 72 * 8 = 576
        
        '''
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]

        if prod / target != target:
            return False

        def dfs(i, prod):
            if prod == target:
                return True

            if i == len(nums):
                return False

            return dfs(i + 1, prod) or dfs(i + 1, prod * nums[i])

        return dfs(0, 1)
        
        