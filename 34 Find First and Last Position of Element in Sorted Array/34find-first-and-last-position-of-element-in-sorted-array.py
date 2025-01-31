class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the leftmost index
        def findLeft(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l

        # Helper function to find the rightmost index
        def findRight(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r

        # Find the left and right positions
        left = findLeft(nums, target)
        right = findRight(nums, target)

        # If the target is not found, return [-1, -1]
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]
