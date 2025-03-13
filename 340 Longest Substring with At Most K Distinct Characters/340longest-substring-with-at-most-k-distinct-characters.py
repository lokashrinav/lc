class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        hmap = defaultdict(int)
        saved = 0
        l = 0
       
        for r in range(len(s)):
            hmap[s[r]] += 1

            while len(hmap) > k:
                hmap[s[l]] -= 1
                if hmap[s[l]] == 0:
                    del hmap[s[l]]
                l += 1

            saved = max(saved, r - l + 1)
        
        return saved
                