class Solution:
    def countSubstrings(self, s: str) -> int:

        num = 0
        for i in range(len(s)):
            start = i
            end = i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                length = end - start + 1
                num += 1
                start -= 1
                end += 1

        for i in range(len(s)):
            start = i
            end = i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                length = end - start + 1
                num += 1
                start -= 1
                end += 1
        return num
            




        