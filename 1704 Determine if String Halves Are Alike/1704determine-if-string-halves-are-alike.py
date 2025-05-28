class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowels = "aeiouAEIOU"

        count = 0
        for i in range(len(s) // 2):
            if s[i] in vowels:
                count += 1
        
        for i in range(len(s) // 2, len(s)):
            if s[i] in vowels:
                count -= 1

        return True if count == 0 else False 
        

        

        