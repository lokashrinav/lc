class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hmap = Counter(nums)

        for num in hmap:
            if hmap[num] % 2:
                return False
        
        return True