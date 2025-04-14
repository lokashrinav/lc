class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - \
                (a[1] - o[1]) * (b[0] - o[0])        

        prev = None
        for i in range(len(points)):
            c = cross(points[i - 1], points[i], points[((i + 1) % len(points))])
            if c:
                diff = 1 if c > 0 else -1
                if prev is not None:
                    if prev ^ diff:
                        return False
                else:
                    prev = 1 if c > 0 else -1

        return True

        
        '''

        0, 0
        5, 5
        0, 10

        5, -5
        -5, -5

        '''

            
