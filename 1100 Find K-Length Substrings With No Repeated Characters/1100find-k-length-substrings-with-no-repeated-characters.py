class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        if k > len(s):
            return 0

        count = 0
        total = 0
        hmap = defaultdict(int)
        for i in range(k):
            hmap[s[i]] += 1
            if hmap[s[i]] == 2:
                count += 1
        
        if not count:
            total += 1
        
        for i in range(k, len(s)):
            hmap[s[i]] += 1
            if hmap[s[i]] == 2:
                count += 1
            hmap[s[i - k]] -= 1
            if hmap[s[i - k]] == 1:
                count -= 1
            if not count:
                total += 1
        
        return total

