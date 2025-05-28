class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:

        minNum = 0
        count = 0
        for i in range(len(rectangles)):
            minRect = min(rectangles[i])
            if minRect > minNum:
                minNum = minRect
                count = 1
            elif minRect == minNum:
                count += 1
        
        return count
        