class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        def helper(arr, index):
            if index == len(nums):
                final.append(arr.copy())
                return
            arr.append(nums[index])
            helper(arr, index + 1)
            saved = arr.pop()
            while index < len(nums) and nums[index] == saved:
                index += 1
            helper(arr, index)
        
        helper([], 0)
        return final
        