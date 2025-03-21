class Solution:
    def canWin(self, currentState: str) -> bool:

        arr = list(currentState)
        memo = {}
        def dfs(curr):
            if curr in memo:
                return memo[curr]
            
            for i in range(len(curr) - 1):
                if curr[i:i+2] == '++':
                    if not dfs(curr[:i] + '--' + curr[i+2:]):
                        memo[curr] = True
                        return memo[curr]
            
            memo[curr] = False

            return memo[curr]

        return dfs(currentState)