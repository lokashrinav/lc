class Solution:
    def maxSum(self, nums: List[int]) -> int:
        num = None
        for i in range(len(nums)):
            if nums[i] > 0:
                num = nums[i]

        if num is None:
            return max(nums)

        idk = sum(num for num in set(nums) if num > 0)

        return idk