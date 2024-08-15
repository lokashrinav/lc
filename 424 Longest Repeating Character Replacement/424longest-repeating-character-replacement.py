class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        greatestCount = 0
        l, r = 0, 0
        while r < len(s):
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            greatestCount = max(greatestCount, hmap[s[r]])
            while (r - l + 1) - greatestCount > k:
                hmap[s[l]] -= 1
                l += 1
            r += 1
        return (r - l)



        