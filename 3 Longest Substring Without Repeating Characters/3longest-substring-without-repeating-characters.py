class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLength = 0
        current = set()
        currLen = 0
        while r < len(s):
            while s[r] in current:
                current.remove(s[l])
                l += 1
                currLen -= 1
            current.add(s[r])
            currLen += 1
            maxLength = max(currLen, maxLength)
            r += 1
        maxLength = max(currLen, maxLength)
        return maxLength

        

        