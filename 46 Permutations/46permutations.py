class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []
        arr = [True] * len(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            
            for i in range(len(nums)):
                if arr[i]:
                    curr.append(nums[i])
                    arr[i] = False
                    dfs(curr)
                    arr[i] = True
                    curr.pop()
        
        dfs(curr)

        return res