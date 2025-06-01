class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        total = 0
        res = set()
        for i in range(len(words)):
            for p in range(len(words)):
                if i != p and words[i] in words[p]:
                    res.add(words[i])
        
        return list(res)



        