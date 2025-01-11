class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        count = k
        hmap = {}
        for i in range(len(s)):
            hmap[s[i]] = hmap.get(s[i], 0) + 1
        
        for key, val in hmap.items():
            if val % 2:
                count -= 1
        
        if count < 0:
            return False
        
        return True
            
