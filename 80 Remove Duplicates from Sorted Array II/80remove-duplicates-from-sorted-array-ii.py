class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # If 2 or fewer elements, all are valid
        
        j = 2  # Start placing valid elements from index 2
        
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1  # Move the write pointer forward
        
        return j