class Solution:
    def climbStairs(self, n: int) -> int:

        # dp[i] = dp[i - 1] + dp[i - 2]

        prev1, prev2 = 1, 1

        for i in range(2, n + 1):
            val = prev1 + prev2
            prev1 = prev2
            prev2 = val
                
        return prev2
