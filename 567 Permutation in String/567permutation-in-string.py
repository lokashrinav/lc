class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        hmap2 = {}
        for i in s1:
            hmap[i] = hmap.get(i, 0) + 1
        
        if len(s2) < len(s1):
            return False
        
        for i in range(len(s1)):
            hmap2[s2[i]] = hmap2.get(s2[i], 0) + 1
                
        if hmap == hmap2:
            return True
        
        for i in range(len(s2) - len(s1)):
            start = i
            end = i + len(s1)
            hmap2[s2[start]] -= 1
            if hmap2[s2[start]] == 0:
                del hmap2[s2[start]]
            hmap2[s2[end]] = hmap2.get(s2[end], 0) + 1
            if hmap2 == hmap:
                return True
        
        return False


        
        

        
        