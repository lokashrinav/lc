class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            elem = str(nums[i])
            total = 0
            for e in elem:
                total += int(e)
            if i == total:
                return i

        return -1