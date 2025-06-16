class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        word1 = list(word1)[::-1]
        word2 = list(word2)[::-1]
        res = []

        while word1 or word2:
            if word1 and not word2:
                res.append(word1.pop())
            elif word2 and not word1:
                res.append(word2.pop())
            elif word1[-1] > word2[-1]:
                res.append(word1.pop())
            elif word1[-1] == word2[-1]:
                if word1[::-1] > word2[::-1]:
                    res.append(word1.pop())
                else:
                    res.append(word2.pop())
            else:
                res.append(word2.pop())

        return ''.join(res)
            


        
        