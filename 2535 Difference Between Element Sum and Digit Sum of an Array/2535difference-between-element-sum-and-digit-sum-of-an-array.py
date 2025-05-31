class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        def func(nums):
            total = 0
            for elem in nums:
                for p in str(elem):
                    total += int(p)
            return total

        return abs(sum(nums) - func(nums))