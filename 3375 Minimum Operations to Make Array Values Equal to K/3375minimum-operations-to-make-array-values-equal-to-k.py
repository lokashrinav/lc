class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        for elem in nums:
            if elem < k:
                return -1
        
        hset = set()
        for elem in nums:
            if elem > k:
                hset.add(elem)
        
        return len(hset)



        