class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hmap1 = Counter(ransomNote)
        hmap2 = Counter(magazine)

        for key, val in hmap1.items():
            if key not in hmap2:
                return False
            if hmap2[key] < val:
                return False
        
        return True