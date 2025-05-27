class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # -3 -1 -4 4 2

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        startVal = 1

        if min(nums) <= 0:
            startVal = abs(min(nums)) + 1

        return startVal


        