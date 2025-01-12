class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        str1 = ""
        for i in range(numRows):
            increment = 2 * (numRows - 1)
            for p in range(i, len(s), increment):
                str1 += s[p]
                if i > 0 and i < numRows - 1 and p + increment - 2 * i < len(s):
                    str1 += s[p + increment - 2 * i]
        
        return str1
        