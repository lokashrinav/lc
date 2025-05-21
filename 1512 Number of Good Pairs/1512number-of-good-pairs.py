class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0

        hmap = Counter(nums)

        for key, val in hmap.items():
            total += (val * (val - 1)) // 2
        
        return total
        