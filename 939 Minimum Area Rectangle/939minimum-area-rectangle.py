class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        setPoints = set((x, y) for x, y in points)
        minArea = float('inf')

        for i in range(len(points)):
            x1, y1 = points[i]
            for p in range(i + 1, len(points)):
                x2, y2 = points[p]
                if x2 != x1 and y2 != y1:
                    if (x1, y2) in setPoints and (x2, y1) in setPoints:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        minArea = min(area, minArea)
        return minArea if minArea != float('inf') else 0


        