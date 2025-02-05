class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = defaultdict(int)
        hmap[0] = -1

        count = 0
        for i in range(len(nums)):
            count = (nums[i] + count) % k
            if count in hmap and i - hmap[count] >= 2:
                return True
            if count not in hmap:
                hmap[count] = i
        
        return False

        