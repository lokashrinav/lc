class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        def is_zero(k, nums, queries):
            arr = [0] * len(nums)
            for i in range(k):
                l, r, am = queries[i]
                arr[l] += am
                if r + 1 < len(nums):
                    arr[r + 1] -= am
            
            curr = 0
            for i in range(len(arr)):
                curr += arr[i]
                if nums[i] > curr:
                    return False

            return True

        

        l, r = 0, len(queries)
        ans = -1

        while l <= r:
            m = (l + r) // 2
            if is_zero(m, nums, queries):
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans