class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        hmap1 = Counter(word1)
        hmap2 = Counter(word2)

        for key, val in hmap1.items():
            if key not in hmap2:
                hmap2[key] = 0

        for key, val in hmap2.items():
            if key not in hmap1:
                hmap1[key] = 0
        
        for key, val in hmap1.items():
            if abs(hmap1[key] - hmap2[key]) > 3:
                return False
        
        return True

        