class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0 for _ in range(len(nums) + 1)] for _ in range(3)]

        for i in range(len(nums) - 1, -1, -1):
            for p in range(2, -1, -1):
                num = dp[p][i + 1] % 3
                dp[num][i] = max(dp[p][i + 1], dp[num][i])
                num = (dp[p][i + 1] + nums[i]) % 3
                dp[num][i] = max(dp[p][i + 1] + nums[i], dp[num][i])
        return dp[0][0]
        