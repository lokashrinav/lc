class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        set1 = set()

        if len(s) < len(t):
            return 0
        elif len(s) == len(t) and s != t:
            return 0
        
        dp = [[0 for i in range(len(t) + 1)] for p in range(len(s) + 1)]

        dp[-1][-1] = 1

        for i in range(len(s)):
            dp[i][-1] = 1

        for p in range(len(s) - 1, -1, -1):
            for i in range(len(t) - 1, -1, -1):
                set1.add(s[p])
                if t[i] == s[p] and s[p] in set1:
                    dp[p][i] = dp[p + 1][i + 1] + dp[p + 1][i]
                elif t[i] == s[p]:
                    dp[p][i] = max(dp[p + 1][i], dp[p][i + 1], dp[p + 1][i + 1])
                else:
                    dp[p][i] = dp[p + 1][i]

        return dp[0][0]

        