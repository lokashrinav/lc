class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        maxNum = max(nums)
        minNum = min(nums)

        if maxNum - k > minNum + k:
            return abs((maxNum - k) - (minNum + k))
        else:
            return 0

        