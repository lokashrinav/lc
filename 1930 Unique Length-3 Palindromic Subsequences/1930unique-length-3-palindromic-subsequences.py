class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hmap = Counter(s)

        hset = set()
        res = set()

        count = 0
        for i in range(len(s) - 1):
            hmap[s[i]] -= 1 
            for key in hmap.keys():
                if hmap[key] > 0 and key in hset:
                    res.add(key + s[i] + key)  
            hset.add(s[i])            
        return len(res)




           
