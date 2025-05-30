class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        hset = set()
        nums.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            hset.add((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        
        return len(hset)


        