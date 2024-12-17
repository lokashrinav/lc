class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}
        def dfs(n):
            if n == 1:
                return 0
            if n in memo:
                return memo[n]
            if n % 2:
                memo[n] = 1 + min(dfs(n + 1), dfs(n - 1))
                return memo[n]
            else:
                memo[n] = 1 + dfs(n / 2)
                return memo[n]
        
        return dfs(n)
        