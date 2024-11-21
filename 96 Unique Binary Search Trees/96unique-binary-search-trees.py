class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        
        for i in range(2, n + 1):
            total = 0
            for p in range(1, i + 1):
                left = p - 1
                right = i - p
                total += dp[left] * dp[right]
            dp[i] = total
        print(dp)
        return dp[n]       
        