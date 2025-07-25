class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n + 1)
        offset = 1
        idk = 1
        for i in range(1, n + 1):
            dp[i] = dp[i - offset] + 1
            if dp[i] == idk:
                offset *= 2
                idk += 1
        
        return dp
