class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        '''

        5, 6, 2, 0

        '''

        visited = set()

        def dfs(num, curr):
            if nums[num] not in visited:
                visited.add(nums[num])
                return dfs(nums[num], curr + 1)
            else:
                return curr

        maxNum = 0
        for i in range(len(nums)):
            if nums[i] not in visited:                
                visited.add(nums[i])
                maxNum = max(maxNum, dfs(nums[i], 1))
        
        return maxNum

        