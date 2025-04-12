class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        sum1 = sum(nums)

        return sum1 % k
            