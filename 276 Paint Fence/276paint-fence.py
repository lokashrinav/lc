class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        memo = {}
        def dfs(num, curr, prev):
            if num == 0:
                return 1
            if (num, curr) in memo:
                return memo[(num, curr)]

            total = 0

            for i in range(k):
                if i == prev and curr:
                    continue
                if i == prev:
                    total += dfs(num - 1, True, i)
                else:
                    total += dfs(num - 1, False, i)
            
            memo[(num, curr)] = total

            return total
        
        return dfs(n, False, None)

        