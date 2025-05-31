class Solution:
    def minOperations(self, nums: List[int]) -> int:

        total = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                total += (nums[i - 1] - nums[i] + 1)
                nums[i] += (nums[i - 1] - nums[i] + 1)
            #print(nums)
                
        return total
        