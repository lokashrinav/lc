class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        def dfs(curr, index):
            if index == len(nums):
                final.append(curr.copy())
                return
            curr.append(nums[index])
            dfs(curr, index + 1)
            curr.pop()
            dfs(curr, index + 1)
        
        dfs([], 0)
        print(final)
        return final
        