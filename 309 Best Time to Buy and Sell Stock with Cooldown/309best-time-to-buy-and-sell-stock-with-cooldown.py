class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for i in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):

            if i < len(prices) + 1:
                dp[i][1] = max(dp[i + 1][1], -prices[i] + dp[i + 1][0])
            else:
                dp[i][1] = max(0, -prices[i])        

            if i < len(prices) - 1:
                cooldown = max(dp[i + 2][1] + prices[i], dp[i + 1][0])
            elif i < len(prices):
                cooldown = dp[i + 1][0]
            else:
                cooldown = 0

            dp[i][0] = max(cooldown, prices[i])

        return dp[0][1]

            



        