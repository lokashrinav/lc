class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        last = 1

        for i in range(len(nums)):
            if abs(nums[i]) == len(nums):
                last *= -1
            elif nums[abs(nums[i])] > 0:
                nums[abs(nums[i])] *= -1
        
        print(nums)

        if last > 0:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        
        return nums.index(0)
