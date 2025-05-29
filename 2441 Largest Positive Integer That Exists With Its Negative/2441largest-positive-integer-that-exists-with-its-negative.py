class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        maxNum = -1
        hset = set(nums)

        for elem in nums:
            if elem > maxNum and -elem in hset:
                maxNum = elem
        
        return maxNum

        