class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        arr2 = arr[::]
        arr2.sort()

        hmap = {}
        count = 0

        for i in range(len(arr)):
            if arr2[i] not in hmap:
                hmap[arr2[i]] = count + 1
                count += 1
                
        res = []

        for elem in arr:
            res.append(hmap[elem])
        
        return res
        
        