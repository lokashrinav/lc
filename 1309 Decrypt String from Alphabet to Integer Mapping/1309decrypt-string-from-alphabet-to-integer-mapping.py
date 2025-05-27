class Solution:
    def freqAlphabets(self, s: str) -> str:

        str1 = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
                i += 1
                continue
            if i + 2 >= len(s):
                str1 += chr(int(s[i]) + 96)
            elif s[i + 2] == "#":
                str1 += chr(int(s[i:i+2]) + 96)
                i += 2
            else:
                str1 += chr(int(s[i]) + 96)
            i += 1
        
        return str1
            