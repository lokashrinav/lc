class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        minNum = min(nums)
        con = minNum + len(nums) - 1
        hset = set()

        for elem in nums:
            if elem > con:
                return False
            hset.add(elem)
        
        return len(hset) == con - minNum + 1
        