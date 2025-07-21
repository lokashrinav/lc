class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        '''

        dp[i][j] = 
            if word1[i] == word2[j]: dp[i][j] = dp[i - 1][j - 1]
            elif word1[i] != word2[j]: dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])
            elif j == -1: dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])
            elif i == -1: dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])
        '''

        '''if not word1 and not word2 or word1 == word2:
            return 0'''

        dp = [[0] * (len(word1) + 1) for i in range(len(word2) + 1)]

        for i in range(len(dp)):
            dp[i][0] = i

        for i in range(len(dp[0])):
            dp[0][i] = i

        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        print(dp)
        
        return dp[-1][-1]
