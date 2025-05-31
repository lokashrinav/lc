class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        hmap = Counter(nums)

        for key, val in hmap.items():
            if val > 2:
                return False
        
        return True
        