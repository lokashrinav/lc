class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 1:
            return 1

        
        hmap = defaultdict(set)
        for i in range(len(points)):
            nx, ny = points[i]
            for p in range(len(points)):
                if i == p:
                    continue
                dx, dy = points[p]
                if dx - nx == 0:
                    hmap[("h", nx)].add(tuple(points[i]))
                    hmap[("h", nx)].add(tuple(points[p]))
                else:
                    calc1 = (dy - ny) / (dx - nx)
                    # y = calc1 * x + b
                    # ny - calc1 * nx = b
                    hmap[(calc1, ny - calc1 * nx)].add(tuple(points[i]))
                    hmap[(calc1, ny - calc1 * nx)].add(tuple(points[p]))
        
        # n * (n + 1) // 2 = y max(hmap.values())
        # n ** 2 + n = 2 * y = val

        #print(hmap)
        hmap2 = {}

        maxNum = 0
        for elem in hmap:
            maxNum = max(maxNum, len(hmap[elem]))
            hmap2[elem] = len(hmap[elem])
        
        print(hmap2)
        
        return maxNum






        