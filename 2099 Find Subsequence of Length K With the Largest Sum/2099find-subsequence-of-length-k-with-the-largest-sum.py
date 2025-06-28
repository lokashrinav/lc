class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        prev = nums[::]
        nums = sorted(nums)
        hmap = defaultdict(int)

        for i in range(len(nums) - 1, len(nums) - 1 - k, -1):
            hmap[nums[i]] += 1
        
        res = []

        for i in range(len(prev)):
            if prev[i] in hmap and hmap[prev[i]]:
                hmap[prev[i]] -= 1
                res.append(prev[i])
        
        return res




        