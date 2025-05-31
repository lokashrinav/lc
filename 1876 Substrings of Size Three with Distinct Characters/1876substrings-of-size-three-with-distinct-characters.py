class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        hmap = Counter(s[:3])
        count = 0

        if len(hmap) == 3:
            count += 1

        for i in range(3, len(s)):
            hmap[s[i]] += 1
            hmap[s[i - 3]] -= 1
            if hmap[s[i - 3]] == 0:
                del hmap[s[i - 3]]
            
            if len(hmap) == 3:
                count += 1
            
        return count

        