class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        maxDiff = 0

        for i in range(1, len(nums)):
            maxDiff = max(maxDiff, abs(nums[i] - nums[i - 1]))
        
        maxDiff = max(maxDiff, abs(nums[0] - nums[-1]))

        return maxDiff
        

        