class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []
        
        res = []
        hmap = defaultdict(int)
        hrat = Counter(p)
        for i in range(len(p)):
            hmap[s[i]] += 1
        
        diff = 0
        for key, val in hrat.items():
            if key not in hmap:
                diff += 1
            elif key in hmap and hmap[key] != hrat[key]:
                diff += 1

        for key, val in hmap.items():
            if key not in hrat:
                diff += 1
        
        if diff == 0:
            res.append(0)
        
        for i in range(len(p), len(s)):
            # print(diff, hmap, hrat)
            if hmap[s[i]] == hrat.get(s[i], 0):
                diff += 1

            hmap[s[i]] += 1

            if hmap[s[i]] == hrat.get(s[i], 0):
                diff -= 1

            if hmap[s[i - len(p)]] == hrat.get(s[i - len(p)], 0):
                diff += 1

            hmap[s[i - len(p)]] -= 1

            if hmap[s[i - len(p)]] == hrat.get(s[i - len(p)], 0):
                diff -= 1

            if hmap[s[i - len(p)]] == 0:
                del hmap[s[i - len(p)]]

            if diff == 0:
                res.append(i - len(p) + 1)
        
        # print(diff, hmap, hrat)

        return res
            
        