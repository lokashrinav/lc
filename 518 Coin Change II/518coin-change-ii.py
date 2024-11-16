class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        if amount == 0:
            return 1

        cache = {}

        def dfs(left, ind):
            if ind < 0 or left < 0:
                return 0
            if (left, ind) in cache:
                return cache[(left, ind)]
            if left == 0:
                return 1
            include_current = dfs(left - coins[ind], ind) 
            exclude_current = dfs(left, ind - 1)      
            cache[(left, ind)] = include_current + exclude_current
            return cache[(left, ind)]
            
        return dfs(amount, len(coins) - 1)



        