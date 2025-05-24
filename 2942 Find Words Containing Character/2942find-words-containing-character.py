class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        count = 0
        res= []
        for word in words:
            if x in word:
                res.append(count)
            count += 1
        
        return res