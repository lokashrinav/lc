class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        hmap = defaultdict(int)
        str1 = ""
        for i in range(len(s)):
            str1 += s[i]
            for p in range(len(str1)):
                curr = str1[p:]
                hmap[curr] += 1
        
        maxNum = max(hmap.values())

        if maxNum == 1:
            return 0
        
        fun = 0
        for key, val in hmap.items():
            if val > 1:
                fun = max(fun, len(key))
        
        return fun
                