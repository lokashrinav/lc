class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        for i in range(min(len(word1), len(word2)) * 2):
            if i % 2 == 0:
                s += word1[i // 2]
            else:
                s += word2[i // 2]
        if len(word2) == len(word1):
            return s
        elif len(word1) > len(word2):
            return s + word1[(i // 2) + 1:]
        else:
            return s + word2[(i // 2) + 1:] 
        