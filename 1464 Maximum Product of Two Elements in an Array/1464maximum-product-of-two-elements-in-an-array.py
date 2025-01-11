class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minNum = 0
        minNum2 = 0
        for i in range(len(nums)):
            if nums[i] >= minNum:
                minNum2 = minNum
                minNum = nums[i]
            elif nums[i] >= minNum2:
                minNum2 = nums[i]

        return (minNum - 1) * (minNum2 - 1)