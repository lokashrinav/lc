class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        hmap = defaultdict(int)
        for i in range(len(trust)):
            hmap[trust[i][0]] += 1

        hmap2 = defaultdict(int)
        for i in range(len(trust)):
            hmap2[trust[i][1]] += 1

        for key, val in hmap2.items():
            if val == n - 1 and hmap[key] == 0:
                return key
        
        return -1
            

        