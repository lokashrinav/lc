class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        total = 0
        for i in range(len(nums)):
            if nums[i] % 3 != 0:
                total += 1
        
        return total
        