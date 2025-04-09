class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        idk = s.split(" ")
        hmap1 = defaultdict(int)
        hmap2 = defaultdict(int)

        if len(idk) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in hmap1 or idk[i] in hmap2:
                if idk[i] == hmap1[pattern[i]] and hmap2[idk[i]] == pattern[i]: 
                    pass
                else:
                    return False
            else:
                hmap1[pattern[i]] = idk[i]
                hmap2[idk[i]] = pattern[i]


        return True
                
            
