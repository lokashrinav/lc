class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            start, end = i, i
            curr = ""
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if start == end:
                    curr += s[start]
                else:
                    curr = s[start] + curr + s[end]
                if end - start + 1 > len(longest):
                    longest = curr
                start -= 1
                end += 1

        for i in range(len(s)):
            start, end = i, i + 1
            curr = ""
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if start == end:
                    curr += s[start]
                else:
                    curr = s[start] + curr + s[end]
                if end - start + 1 > len(longest):
                    longest = curr
                start -= 1
                end += 1
        return longest


        
        