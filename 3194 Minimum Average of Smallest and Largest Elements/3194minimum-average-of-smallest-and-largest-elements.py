class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        nums.sort()

        minAvg = float('inf')

        l, r = 0, len(nums) - 1

        while l < r:
            avg = (nums[l] + nums[r]) / 2
            minAvg = min(avg, minAvg)
            l += 1
            r -= 1
        
        return minAvg
        