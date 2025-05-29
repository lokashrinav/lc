class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        hmap = defaultdict(int)

        total = 0

        for i in range(len(nums)):
            total += hmap[nums[i] - k]
            total += hmap[nums[i] + k]

            hmap[nums[i]] += 1
        
        return total