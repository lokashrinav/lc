class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        res = []
        hmap = {}

        for i in range(k):
            if nums[i] not in hmap:
                hmap[nums[i]] = 0
            hmap[nums[i]] += 1
        
        res.append(len(hmap))
        
        for i in range(k, len(nums)):
            hmap[nums[i - k]] -= 1
            if hmap[nums[i - k]] == 0:
                del hmap[nums[i - k]]
            
            if nums[i] not in hmap:
                hmap[nums[i]] = 0
            hmap[nums[i]] += 1

            res.append(len(hmap))
        
        return res

        
        