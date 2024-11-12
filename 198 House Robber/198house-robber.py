class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            if i >= 3:
                dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            else:
                dp[i] = dp[i - 2] + nums[i]
        
        return max(dp[-1], dp[-2])

        