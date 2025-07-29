class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        dp[i][0][k] -> we are at index i, we are not holding a stock, we completed k transactions
        dp[i][1][k] -> we are at index i, we are holding a stock, we completed k transactions

        if k == max_k:
            dp[i][bool][k] = dp[i + 1][bool][k]

        dp[i][0][k] = max(dp[i + 1][1][k] - prices[i], dp[i + 1][0][k])
        dp[i][1][k] = max(dp[i + 1][0][k + 1] + prices[i], dp[i + 1][1][k])
        '''

        cache = {}
        def dfs(ind, have_stock, transaction_count):
            if (ind, have_stock, transaction_count) in cache:
                return cache[(ind, have_stock, transaction_count)]

            calc = None
            if ind == len(prices):
                calc = 0
            elif k == transaction_count:
                calc = 0
            elif have_stock == 0:
                calc = max(dfs(ind + 1, 1, transaction_count) - prices[ind], dfs(ind + 1, 0, transaction_count))
            else:
                calc = max(dfs(ind + 1, 0, transaction_count + 1) + prices[ind], dfs(ind + 1, 1, transaction_count))
            
            cache[(ind, have_stock, transaction_count)] = calc

            return calc
        
        calc = dfs(0, 0, 0)

        print(cache)

        return calc

        '''cache = {}
        def dfs(ind, have_stock, transaction_count):
            if (ind, have_stock, transaction_count) in cache:
                return cache[(ind, have_stock, transaction_count)]

            calc = None
            if ind == len(prices):
                calc = 0
            elif transaction_count == k:  # No more transactions allowed
                calc = 0
            elif have_stock == 0:  # Don't have stock - can buy
                calc = max(dfs(ind + 1, 1, transaction_count) - prices[ind], 
                        dfs(ind + 1, 0, transaction_count))
            else:  # Have stock - can sell
                calc = max(dfs(ind + 1, 0, transaction_count + 1) + prices[ind], 
                        dfs(ind + 1, 1, transaction_count))  # Fixed: 'ind' not 'i'
            
            cache[(ind, have_stock, transaction_count)] = calc
            return calc
        
        return dfs(0, 0, 0)'''

                    


                