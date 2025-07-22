class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''

        dp[i][j] = dp[i - 1][j - 1] if text1[i] == text[j] else max(dp[i - 1][j], dp[i][j - 1])

        dp[i][0] = 0

        dp[0][j] = 0

        '''

        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for p in range(1, len(text2) + 1):
                if text1[i - 1] == text2[p - 1]:
                    dp[i][p] = 1 + dp[i - 1][p - 1]
                else:
                    dp[i][p] = max(dp[i - 1][p], dp[i][p - 1])

        #print(dp)

        return dp[-1][-1]
