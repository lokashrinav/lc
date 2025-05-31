class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        for i in range(len(points)):
            for p in range(i + 1, len(points)):
                if points[i] == points[p]:
                    return False

        if (points[0][0] - points[1][0]) != 0:
            slope1 = (points[0][1] - points[1][1]) / (points[0][0] - points[1][0])
        else:
            slope1 = None

        if (points[2][0] - points[1][0]) != 0:
            slope2 = (points[2][1] - points[1][1]) / (points[2][0] - points[1][0])
        else:
            slope2 = None

        if (points[2][0] - points[0][0]) != 0:
            slope3 = (points[2][1] - points[0][1]) / (points[2][0] - points[0][0])
        else:
            slope3 = None

        if slope1 == slope2 == slope3:
            return False
        
        return True

        