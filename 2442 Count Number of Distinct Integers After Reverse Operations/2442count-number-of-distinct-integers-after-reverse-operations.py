class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        hset = set(nums)
        for i in range(len(nums)):
            s = str(nums[i])
            hset.add(int(s[::-1]))
        
        return len(hset)

        