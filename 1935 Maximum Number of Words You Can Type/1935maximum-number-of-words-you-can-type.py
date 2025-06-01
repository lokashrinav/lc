class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        s = text.split(" ")
        total = 0

        for word in s:
            flag = True
            for c in word:
                if c in brokenLetters:
                    flag = False
            
            if flag:
                total += 1
        
        return total

        