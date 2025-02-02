class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')

        for i in range(len(nums)):
            if nums[i] in (first, second, third):
                continue
            if nums[i] > first:
                first, second, third = nums[i], first, second
            elif nums[i] > second:
                second, third = nums[i], second
            elif nums[i] > third:
                third = nums[i]

        return third if third != float('-inf') else first