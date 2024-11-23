class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[-1][-1] = True

        for i in range(len(s1), -1, -1):
            for p in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + p] and dp[i + 1][p]:
                    dp[i][p] = True
                if p < len(s2) and s2[p] == s3[i + p] and dp[i][p + 1]:
                    dp[i][p] = True
            
        return dp[0][0]



        
        
        
        