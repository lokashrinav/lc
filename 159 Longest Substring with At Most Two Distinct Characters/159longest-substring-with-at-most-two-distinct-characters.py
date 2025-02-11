class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        hmap = defaultdict(int)
        changed = None
        p2 = 0
        maxCount = 0
        for i in range(len(s)):
            hmap[s[i]] += 1
            while len(hmap) == 3:
                hmap[s[p2]] -= 1
                if hmap[s[p2]] == 0:
                    del hmap[s[p2]]
                p2 += 1

            maxCount = max(i - p2 + 1, maxCount)
        
        return maxCount


