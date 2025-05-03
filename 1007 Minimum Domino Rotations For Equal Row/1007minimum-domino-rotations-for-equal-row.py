class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        hmap = defaultdict(int)
        for i in range(len(tops)):
            if tops[i] == bottoms[i]:
                hmap[tops[i]] += 1
            else:
                hmap[tops[i]] += 1
                hmap[bottoms[i]] += 1
        
        flag = False
        maxCount = float('inf')
        for key, val in hmap.items():
            if val == len(tops):
                flag = True
                maxCount = min(maxCount, len(tops) - tops.count(key), len(bottoms) - bottoms.count(key))
        
        if not flag:
            return -1
        
        return maxCount