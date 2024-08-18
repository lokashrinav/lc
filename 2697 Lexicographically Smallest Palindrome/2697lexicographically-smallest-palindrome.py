class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        d = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if d[l] != d[r]:
                if d[r] < d[l]:
                    d[l] = d[r]
                else:
                    d[r] = d[l]
            l += 1
            r -= 1
        return ''.join(d)
        