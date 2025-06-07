class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        words = set(words)

        for i in range(len(text)):
            for p in range(i, len(text)):
                if text[i:p+1] in words:
                    res.append((i, p))
        
        return res