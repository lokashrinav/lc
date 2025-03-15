class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRob(nums, m, k):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= m:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k

        l, r = min(nums), max(nums)
        while l < r:
            m = (l + r) // 2
            if canRob(nums, m, k):
                r = m 
            else:
                l = m + 1

        return l