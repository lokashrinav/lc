class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        '''

        O(n) solution

        for a new point:

        we find all other points that are on same y-axis as current point

        we count all other points that are on a different y-axis

        O(n)
        
        '''

        hmap = defaultdict(int)
        others = 0
        total = 0
        for i in range(len(points)):
            x, y = points[i]
            curr = hmap[y]

            if curr >= 1 and others - (curr * (curr - 1) // 2) > 0:
                '''
                1 -> 0
                2 -> 1 + 0
                3 -> 2 + 1
                4 -> 3 + 2 + 1
                
                '''
                sub = (curr * (curr - 1) // 2)
                total = (total + (curr * (others - sub))) % MOD
            
            hmap[y] += 1
            
            if hmap[y] >= 2:
                others += hmap[y] - 1

            #print(hmap, others, total)
            
        return total
                

        
            
        