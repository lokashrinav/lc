class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False

        hmap = {}
        hmap2 = {}
        for i in range(len(s)):
            char = s[i]
            if char in hmap:
                if hmap[char] == t[i]:
                    continue
                else:
                    return False
            elif t[i] in hmap2 and hmap2[t[i]] != char:
                return False
            else:
                hmap[char] = t[i]
                hmap2[t[i]] = char
    
        return True
            
        