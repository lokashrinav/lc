class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        hmap[0] = 1
        again = 0
        count = 0
        for i in range(len(nums)):
            again += nums[i]
            count += hmap[again - k]
            hmap[again] += 1
        
        return count

