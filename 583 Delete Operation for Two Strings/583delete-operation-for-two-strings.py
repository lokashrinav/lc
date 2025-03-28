class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for y in range(len(word1)):
            for x in range(len(word2)):
                if word1[y] == word2[x]:
                    dp[y + 1][x + 1] += dp[y][x] + 1
                else:
                    dp[y + 1][x + 1] = max(dp[y][x+1], dp[y+1][x])  
        
        print(max(len(word1), len(word2)))
        print(dp[len(word1)][len(word2)])
        return len(word1) + len(word2) - (dp[len(word1)][len(word2)] * 2)