class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        maxLength = max(len(word) for word in words)
        res = [""] * max(len(words), maxLength)
        
        for p in range(len(words)):
            for i in range(len(words[p])):
                print(len(words), len(words[p]))
                res[i] += words[p][i]
        
        print(res)

        for i in range(len(words)):
            if words[i] != res[i]:
                return False
        
        return True