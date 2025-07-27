class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''

        dp[i][0] = max(dp[i + 1][1] + prices[i] - fee, dp[i + 1][0])
        dp[i][1] = max(-prices[i] + dp[i + 1][0] - fee, dp[i + 1][1])

        '''

        dp = [[0, 0] for i in range(len(prices) + 1)]
        for i in range(len(prices) - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][1] + prices[i], dp[i + 1][0])
            dp[i][1] = max(-prices[i] + dp[i + 1][0] - fee, dp[i + 1][1])
        
        print(dp)

        return dp[0][1]
