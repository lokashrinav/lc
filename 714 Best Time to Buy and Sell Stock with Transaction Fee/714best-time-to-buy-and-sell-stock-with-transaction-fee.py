class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        memo = {}
        def dfs(ind, buy):
            if ind >= len(prices):
                return 0

            if (ind, buy) in memo:
                return memo[(ind, buy)]

            if buy:
                total = -prices[ind] + -fee + dfs(ind + 1, False)
            else:
                total = prices[ind] + dfs(ind + 1, True)
            
            total = max(total, dfs(ind + 1, buy))

            memo[(ind, buy)] = total

            return total
        
        return dfs(0, True)
        