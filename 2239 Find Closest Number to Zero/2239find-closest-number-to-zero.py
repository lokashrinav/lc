class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        saved = nums[0]

        for i in range(1, len(nums)):
            if abs(saved) > abs(nums[i]):
                saved = nums[i]
            elif abs(saved) == abs(nums[i]):
                saved = max(saved, nums[i])

        return saved

        