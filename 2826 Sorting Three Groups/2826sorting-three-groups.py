class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dp = [len(nums)] * 4

        for i in nums:
            dp[i] -= 1
            dp[2] = min(dp[1], dp[2])
            dp[3] = min(dp[2], dp[3])
        
        return dp[3]

        