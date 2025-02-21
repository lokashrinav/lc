class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        minCount = float('inf')
        ind1 = None
        ind2 = None
        for i, word in enumerate(wordsDict):
            if word1 == word:
                ind1 = i
                if ind1 is not None and ind2 is not None:
                    minCount = min(minCount, ind1 - ind2)

            if word2 == word:
                ind2 = i
                if ind1 is not None and ind2 is not None:
                    minCount = min(minCount, ind2 - ind1)
        
        return minCount
