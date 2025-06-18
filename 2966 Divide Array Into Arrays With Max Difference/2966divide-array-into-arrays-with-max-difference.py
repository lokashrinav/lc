class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()

        res = []

        for i in range(0, len(nums), 3):
            lis1 = [nums[i], nums[i + 1], nums[i + 2]]

            if max(lis1) - min(lis1) > k:
                return []
            
            res.append(lis1)
        
        return res