class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        maxLen = 0
        sum1 = 0
        l = 0

        for i in range(len(s)):
            sum1 += abs(ord(s[i]) - ord(t[i]))
            while sum1 > maxCost:
                sum1 -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            
            if l <= i:
                maxLen = max(i - l + 1, maxLen)
        
        return maxLen


        