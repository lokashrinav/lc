class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        total = 0
        for p in patterns:
            if p in word:
                total += 1
        
        return total