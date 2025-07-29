class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp[i][True] = max(dp[i + 1][False] + prices[i], dp[i + 1][True])
        dp[i][False] = max(dp[i + 1][True] - prices[i], dp[i + 1][False])

        dp[i][True][limit] = max(dp[i + 1][False][limit] + prices[i], dp[i + 1][True][limit])
        dp[i][False][limit] = max(dp[i + 1][True][limit] - prices[i], dp[i + 1][False][limit])  

        '''

        # n * 2 * 2

        dp = [[0] * 6 for p in range(len(prices) + 1)]

        for y in range(len(prices) - 1, -1, -1):
            i = y
            dp[y][0] = max(dp[y + 1][0], dp[y + 1][3] - prices[i])
            dp[y][1] = max(dp[y + 1][1], dp[y + 1][4] - prices[i])
            dp[y][2] = dp[y + 1][2]

            dp[y][3] = max(dp[y + 1][3], dp[y + 1][1] + prices[i])
            dp[y][4] = max(dp[y + 1][4], dp[y + 1][2] + prices[i])
            dp[y][5] = dp[y + 1][5]
        
        return dp[0][0]