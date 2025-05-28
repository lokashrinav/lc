class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        hmap = {}
        maxNum = -1

        for i in range(len(s)):
            if s[i] in hmap:
                maxNum = max(i - hmap[s[i]] - 1, maxNum)
            else:
                hmap[s[i]] = i
        
        return maxNum


        