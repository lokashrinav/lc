class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        i, p = 0, 0
        while i < len(s):
            while p < len(s) and s[p] != " ":
                p += 1
            curr = p
            p = p - 1

            while i < p:
                s[i], s[p] = s[p], s[i]
                i += 1
                p -= 1
            
            i, p = curr + 1, curr + 1
        return s

        