class Solution:
    def findValidPair(self, s: str) -> str:
        hmap = Counter(s)

        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                if hmap[s[i]] == int(s[i]) and hmap[s[i + 1]] == int(s[i + 1]):
                    return s[i:i+2]

        return ""
                
        
        