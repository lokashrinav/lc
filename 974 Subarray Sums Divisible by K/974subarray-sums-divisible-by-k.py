class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        hmap = defaultdict(int)
        hmap[0] = 1
        total = 0
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            if prefix % k in hmap:
                total += hmap[prefix % k]
            hmap[prefix % k] += 1
        
        return total
