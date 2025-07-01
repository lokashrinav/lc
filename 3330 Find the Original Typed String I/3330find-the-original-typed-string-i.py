class Solution:
    def possibleStringCount(self, word: str) -> int:

        l, r = 0, 0
        count = 1
        total = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                if count > 1:
                    total += count - 1
                count = 1

        if count > 1:
            total += count - 1
            
        return total
        