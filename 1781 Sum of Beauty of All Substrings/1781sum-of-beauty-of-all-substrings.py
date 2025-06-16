class Solution:
    def beautySum(self, s: str) -> int:

        '''

        1, 1, 1

        '''

        total = 0
        for i in range(len(s)):
            hmap = defaultdict(int)
            for p in range(i, len(s)):
                hmap[s[p]] += 1
                total += (max(hmap.values()) - min(hmap.values()))
        
        return total




        
        