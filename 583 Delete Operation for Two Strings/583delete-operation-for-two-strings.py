class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''

        dp[i][j] = dp[i - 1][j - 1] if word1[i] == word2[i] else 1 + max(dp[i - 1][j], dp[i][j - 1])

        '''
        
        dp = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            for p in range(1, len(word2) + 1):
                if word1[i - 1] == word2[p - 1]:
                    dp[i][p] = 1 + dp[i - 1][p - 1]
                else:
                    dp[i][p] = max(dp[i - 1][p], dp[i][p - 1])

        print(dp)

        return len(word1) + len(word2) - dp[-1][-1] * 2
