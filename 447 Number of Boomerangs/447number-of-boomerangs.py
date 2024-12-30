class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points)):
            hmap = {}
            for j in range(len(points)):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                calc = sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))
                hmap[calc] = hmap.get(calc, 0) + 1

            for key, val in hmap.items():
                if val > 1:
                    count += val * (val - 1)

        return count

        