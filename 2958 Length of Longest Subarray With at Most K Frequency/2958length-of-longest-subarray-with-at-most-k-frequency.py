class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0 
        hmap = defaultdict(int)
        longest = 0
        
        for i in range(len(nums)):
            hmap[nums[i]] += 1
            while hmap[nums[i]] > k:
                hmap[nums[l]] -= 1
                l += 1
            longest = max(longest, i - l + 1)
        
        return longest