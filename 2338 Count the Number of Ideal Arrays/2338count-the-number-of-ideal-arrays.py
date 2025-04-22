class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:

        memo = {}
        mod = (10 ** 9) + 7

        @lru_cache(None)
        def dfs(val, length):
            nonlocal mod
            total = comb(n - 1, length - 1)
            for multi in range(val * 2, maxValue + 1, val):
                total = (total + dfs(multi, length + 1)) % mod

            return total
        
        total = 0
        for i in range(1, maxValue + 1):
            total = (total + dfs(i, 1)) % mod
        
        return total