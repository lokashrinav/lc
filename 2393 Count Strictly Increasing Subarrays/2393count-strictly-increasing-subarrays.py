class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        total = 0
        length = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                length += 1
            else:
                total += length * (length + 1) // 2
                length = 1
        
        total += length * (length + 1) // 2
        
        return total



