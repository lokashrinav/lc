class Solution:
    def getMoneyAmount(self, n: int) -> int:

        memo = {}
        def dfs(l, r):
            if l == r:
                return 0
            if r < l:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            
            minMax = float('inf')
            for i in range(l, r + 1):
                minMax = min(minMax, max(i + dfs(i + 1, r), i + dfs(l, i - 1)))

            memo[(l, r)] = minMax
            return minMax
        
        return dfs(0, n)