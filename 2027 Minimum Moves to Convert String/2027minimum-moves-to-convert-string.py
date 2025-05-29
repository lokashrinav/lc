class Solution:
    def minimumMoves(self, s: str) -> int:

        s = list(s)
        count = s.count("X")

        total = 0
        for i in range(len(s)):
            if s[i] == "X":
                total += 1

                s[i] = "0"

                if i + 1 < len(s):
                    s[i + 1] = "0"

                if i + 2 < len(s):
                    s[i + 2] = "0"
        
        return total
        


        