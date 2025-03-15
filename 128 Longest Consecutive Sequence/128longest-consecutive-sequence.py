class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxNum = 0
        hset = set(nums)

        for elem in hset:
            if elem - 1 not in hset:
                p = 0
                while elem + p in hset:
                    p += 1
                
                maxNum = max(maxNum, p)
        
        return maxNum

        