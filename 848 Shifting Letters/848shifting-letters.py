class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        str1 = ""
        idk = [0]
        for i in range(len(shifts) - 1, -1, -1):
            idk.append(shifts[i] + idk[-1])
        idk.reverse()
        idk.pop()

        for i in range(len(s)):
            str1 += chr((((ord(s[i]) - 97) + idk[i]) % 26) + 97)
        
        return str1
