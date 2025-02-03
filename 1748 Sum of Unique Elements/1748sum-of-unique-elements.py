class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hmap = Counter(nums)

        total = 0
        for key, val in hmap.items():
            if val == 1:
                total += key
        
        return total