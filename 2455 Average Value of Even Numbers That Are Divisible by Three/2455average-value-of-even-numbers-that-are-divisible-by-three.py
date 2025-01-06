class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0 and nums[i] % 2 == 0:
                total += nums[i]
                count += 1
        
        return total // count if count else 0
        