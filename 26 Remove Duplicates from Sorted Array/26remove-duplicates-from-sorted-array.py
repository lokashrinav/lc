class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l, r = 1, 0
        while r < len(nums) - 1:
            if nums[r] != nums[r + 1]:
                nums[l] = nums[r + 1]
                l += 1
            r += 1
        return l 
        