class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        arr = [True] * len(nums)
        nums.sort()

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            
            for i in range(len(nums)):
                if i >= 1 and nums[i] == nums[i - 1] and arr[i - 1]:
                    continue

                if arr[i]:
                    curr.append(nums[i])
                    arr[i] = False
                    dfs(curr)
                    arr[i] = True
                    curr.pop()
        
        dfs(curr)

        return res