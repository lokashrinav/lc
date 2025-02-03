class Solution:
    def trap(self, height: List[int]) -> int:
        p1, p2 = 0, 0
        maxTotal = 0

        while p1 < len(height) and height[p1] == 0:
            p1 += 1

        while p1 < len(height):
            p2 = p1 + 1
            total = 0
            while p2 < len(height) and height[p2] < height[p1]:
                total += height[p1] - height[p2]
                p2 += 1
            if p2 != len(height):
                p1 = p2
                maxTotal += total
            else:
                p1 += 1

        
        return maxTotal
            


        