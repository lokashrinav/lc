class Solution:
    def sortSentence(self, s: str) -> str:

        res = [""] * 10

        words = s.split(" ")
        for word in words:
            res[int(word[-1]) - 1] = word[:-1]
        
        final = ""
        for i in range(len(res)):
            calc = " " if i + 1 < len(res) and res[i + 1] else ""
            final += res[i] + calc
        
        return final
        