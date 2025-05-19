class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:


        total = 0
        for i in range(1, len(points)):
            minNum = min(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
            idk = abs(points[i][0] - points[i - 1][0]) - minNum
            idk2 = abs(points[i][1] - points[i - 1][1]) - minNum
            print(minNum, idk, idk2)
            total += minNum + idk + idk2

        return total

        return total

        