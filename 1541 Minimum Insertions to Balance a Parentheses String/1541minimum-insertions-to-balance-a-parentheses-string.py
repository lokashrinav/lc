class Solution:
    def minInsertions(self, s: str) -> int:
        curr = 0
        total = 0

        i = 0
        while i < len(s):
            c = s[i]
            if c == "(":
                curr += 1
                i += 1
            elif s[i:i+2] == "))":
                if curr == 0:
                    total += 1
                else:
                    curr -= 1
                i += 2
            elif c == ")":
                if curr == 0:
                    total += 2
                else:
                    total += 1
                    curr -= 1
                i += 1
        
        total += curr * 2

        return total
        