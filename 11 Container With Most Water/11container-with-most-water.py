class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxNum = 0

        while l < r:
            maxNum = max(min(height[r], height[l]) * (r - l), maxNum)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return maxNum
        



        

            