class Solution:
    def soupServings(self, n: int) -> float:

        if n >= 10000:
            return 1

        cache = {}
        def dfs(a, b):
            if (a, b) in cache:
                return cache[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            
            total = 0
            for elem in [dfs(a - 100, b), dfs(a - 75, b - 25), dfs(a - 50, b - 50), dfs(a - 25, b - 75)]:
                total += elem
            
            cache[(a, b)] = 0.25 * total
            
            return cache[(a, b)]

        # 50 * 0.01 = 0.5
        # 100 * 0.0625 = 0.625

        return dfs(n, n)