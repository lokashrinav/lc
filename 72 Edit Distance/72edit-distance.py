class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # {h: 1, o: 1, r: 1, s: 1, e:1}
        # {r: 1, o: 1: s: 1}

        '''
           h  o  r  s  e
        r [0, 0, 1, 0, 0, 0]
        o [0, 1, 0, 0, 0, 0]
        s [0, 0, 0, 0, 0, 0]
          [0, 0, 0, 0, 0, 0]

        '''

        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

        for i in range(len(word2)):
            dp[i][-1] = len(word2) - i

        for p in range(len(word1)):
            dp[-1][p] = len(word1) - p


        for p in range(len(word2) - 1, -1, -1):
            for i in range(len(word1) - 1, -1, -1):
                if word1[i] == word2[p]:
                    dp[p][i] = dp[p + 1][i + 1]
                else:
                    dp[p][i] = min(dp[p + 1][i] + 1, dp[p][i + 1] + 1, dp[p + 1][i + 1] + 1)
        
        return dp[0][0]


        '''for i in range(1, len(word2) + 1):
            for p in range(1, len(word1) + 1):
                down = max(dp[i - 1][p], dp[i][p - 1])
                if word1[p - 1] == word2[i - 1]:
                    dp[i][p] = dp[i - 1][p - 1] + 1
                else:
                    dp[i][p] = down
        
        return max(len(word1), len(word2)) - dp[-1][-1]'''

        