class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfa(curr):
            if curr == n:
                return 1
            if curr > n:
                return 0
            if curr in memo:
                return memo[curr]
            memo[curr] = dfa(curr + 1) + dfa(curr + 2)
            return memo[curr]
        return dfa(0)
        
             


            
        