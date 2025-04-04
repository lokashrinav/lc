class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:      
        pointSet = set((x, y) for (x, y) in points)
        hmap = defaultdict(list)
        for i in range(len(points)):
            hmap[points[i][1]].append(points[i][0])

        count = 0
        m = None
        for i in range(len(points)):
            if m is None:
                m = (max(hmap[points[i][1]]) + min(hmap[points[i][1]])) / 2
            diff = abs(m - points[i][0])
            if points[i][0] < m:
                if (m + diff, points[i][1]) in pointSet:
                    count += 1
            else:
                if (m - diff, points[i][1]) in pointSet:
                    count += 1

        return count == len(points)

        
            
                

