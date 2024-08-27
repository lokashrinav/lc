class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        l = r = 0
        farthest = 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
                if i == r:
                    l = r + 1   
                    r = farthest
            jump += 1
            farthest = 0
        
        return jump
        
        