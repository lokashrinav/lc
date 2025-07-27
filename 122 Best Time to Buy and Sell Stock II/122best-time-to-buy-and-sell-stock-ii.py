class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dfs(ind, False) = max(dfs(ind - 1, True) - prices[ind], dfs(ind + 1, False))
        dfs(ind, True) = max(prices[ind] + dfs(ind - 1, True), dfs(ind - 1, False))

        7, 1, 5, 3, 6, 4


        1, 5

        dp[1][0] = 5
        dp[1][1] = 0

        dp[0][0] = 
        dp[0][1] = 

        '''

        dp = [[0, 0] for i in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1] + prices[i])  # Sell: add price
            dp[i][1] = max(dp[i + 1][1], dp[i + 1][0] - prices[i])  # Buy: subtract price
        
        print(dp)

        return dp[0][1]