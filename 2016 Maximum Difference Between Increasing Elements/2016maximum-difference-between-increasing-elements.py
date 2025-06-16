class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        
        prev = nums[-1]
        maxNum = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > prev:
                prev = nums[i]
            elif prev != nums[i]:
                maxNum = max(maxNum, prev - nums[i])
        
        return maxNum
        