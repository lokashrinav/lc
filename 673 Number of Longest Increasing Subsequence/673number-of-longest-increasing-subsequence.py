class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        length = 1
        for i in range(1, len(nums)):
            for p in range(i):
                if nums[i] > nums[p]:
                    dp[i] += dp[p]

        dp = [1] * len(nums)
        dp[0] = 1
        dp2 = [1] * len(nums)
        dp2[0] = 1
        length = 1

        for i in range(1, len(nums)):
            for p in range(i):
                if nums[i] > nums[p]:
                    if dp[p] + 1 > dp[i]:
                        dp[i] = dp[p] + 1
                        dp2[i] = dp2[p]
                    elif dp[i] == dp[p] + 1:
                        dp2[i] += dp2[p]

        maxNum = max(dp)

        smth = 0
        for i in range(len(dp)):
            if dp[i] == maxNum:
                smth += dp2[i]

        return smth

        
            