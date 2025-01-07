class Solution:
    def findLucky(self, arr: List[int]) -> int:

        hmap = {}
        for i in arr:
            hmap[i] = hmap.get(i, 0) + 1
        
        maxKey = -1
        for key, val in hmap.items():
            if key == val:
                maxKey = max(val, maxKey)
        
        return maxKey
        

        