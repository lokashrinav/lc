class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(queries)):
            count = 0
            for p in range(len(points)):
                x, y, r = queries[i]
                dis = (points[p][0] - x) ** 2 + (points[p][1] - y) ** 2
                if r ** 2 >= dis:
                    count += 1
            ans.append(count)
        return ans
            
                    
                