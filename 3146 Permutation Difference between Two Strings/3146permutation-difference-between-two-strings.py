class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        hmap = {}
        for i in range(len(t)):
            hmap[t[i]] = i
        
        total = 0
        for i in range(len(s)):
            total += abs(i - hmap[s[i]])
        
        print(hmap)
        
        return total