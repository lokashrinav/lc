class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        countLower = 0
        countHigher = 0

        for i in range(len(word)):
            if word[i].islower():
                countLower += 1
            else:
                countHigher += 1
        
        if countHigher == 0 or countLower == 0:
            return True
        elif countHigher == 1 and word[0].isupper():
            return True
        else:
            return False
