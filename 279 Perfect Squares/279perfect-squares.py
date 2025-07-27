class Solution:
    def numSquares(self, n: int) -> int:

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            p = 1
            while p * p <= i:
                dp[i] = min(dp[i], 1 + dp[i - (p * p)])
                p += 1
        
        return dp[-1]



        

        