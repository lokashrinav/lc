class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums)

        dp = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp2[0] = nums[0]
        dp2[1] = nums[1]

        for i in range(2, len(nums) - 1):
            if i >= 3:
                dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            else:
                dp[i] = dp[i - 2] + nums[i]
        
        for i in range(2, len(nums)):
            if i == 2:
                dp2[i] = nums[i]
            elif i == 3:
                dp2[i] = dp2[i - 2] + nums[i]
            else:
                dp2[i] = max(dp2[i - 2], dp2[i - 3]) + nums[i]
        print(dp2)
        print(dp)
        return max(max(dp2), max(dp))

    


