class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        hmap = {}

        three = [-1] * 3
        for i in range(len(colors)):
            three[colors[i] - 1] = i
            hmap[i] = three.copy()
        
        three = [-1] * 3
        for i in range(len(colors) - 1, -1, -1):
            three[colors[i] - 1] = i
            for p in range(3):
                if hmap[i][p] == -1 and three[p] != -1:
                    hmap[i][p] = three[p]
                elif hmap[i][p] == -1 and three[p] == -1:
                    continue
                elif hmap[i][p] != -1 and three[p] == -1:
                    continue
                else:
                    if abs(i - hmap[i][p]) > abs(i - three[p]):
                        hmap[i][p] = three[p]

        res = []
        for y, x in queries:
            if hmap[y][x - 1] == -1:
                res.append(-1)
                continue
            res.append(abs(y - hmap[y][x - 1]))
        
        return res
                
        
