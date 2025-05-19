class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, len(nums) - 1
        maxNum = -1

        while l < r:
            if nums[l] + nums[r] >= k:
                r -= 1
            else:
                maxNum = max(nums[l] + nums[r], maxNum)
                l += 1
        
        return maxNum
