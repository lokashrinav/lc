class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''

        triangle[i][p] += min(triangle[i - 1][p - 1], triangle[i - 1][p])

        '''

        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][-1] += triangle[i - 1][-1]
            for p in range(1, len(triangle[i]) - 1):
                triangle[i][p] += min(triangle[i - 1][p - 1], triangle[i - 1][p])
            #print(triangle)
        
        return min(triangle[-1])

        