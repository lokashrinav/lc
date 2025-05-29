class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        count = 0
        for elem in words:
            if elem == s[:len(elem)]:
                count += 1
        
        return count