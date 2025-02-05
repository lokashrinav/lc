class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        final = defaultdict(int)
        maxNum = 1
        for i in range(len(points)):
            hmap = defaultdict(lambda: 1)
            x1, y1 = points[i]
            # (1, 1)
            for p in range(i + 1, len(points)):
                x2, y2 = points[p]
                check = x2 - x1
                if check != 0:
                    slope = (y2 - y1) / (x2 - x1)
                else:
                    slope = float('inf')
                
                hmap[slope] += 1
            
            for key in hmap.keys():
                if key in final:
                    final[key] = max(final[key], hmap[key])
                else:
                    final[key] += hmap[key]
                maxNum = max(final[key], maxNum)
        
        return maxNum 


        
            

            

