class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        hmap = [0] * 3
    
        for i in range(len(nums)):
            hmap[nums[i]] += 1
        
        for i in range(len(nums)):
            while p1 < len(hmap) and hmap[p1] == 0:
                p1 += 1
            nums[i] = p1
            hmap[p1] -= 1
        
        return nums