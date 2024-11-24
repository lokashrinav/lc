class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            buy = max(-prices[i] + dp[i + 1][0], dp[i + 1][1])
            sell = max(prices[i] + dp[i + 1][1], dp[i + 1][0])
            dp[i][1] = buy
            dp[i][0] = sell
                    
        return dp[0][1]



        
        