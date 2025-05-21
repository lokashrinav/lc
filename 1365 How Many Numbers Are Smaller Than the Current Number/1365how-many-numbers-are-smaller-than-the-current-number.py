class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        hset = nums[::]
        
        hset.sort()

        hmap = {}

        for i in range(len(hset)):
            if hset[i] not in hmap:
                hmap[hset[i]] = i
            else:
                hmap[hset[i]] = min(hmap[hset[i]], i)
        
        res = []
        for elem in nums:
            res.append(hmap[elem])
        
        return res




        