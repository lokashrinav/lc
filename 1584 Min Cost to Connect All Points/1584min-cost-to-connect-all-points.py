class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        visited = set()
        minH = [[0, 0]]
        while len(visited) < len(points):
            cost, num = heapq.heappop(minH)
            if num in visited:
                continue
            res += cost
            visited.add(num)
            for j in range(len(points)):
                if j not in visited:
                    ai, bi = points[num]
                    aj, bj = points[j]
                    neighbor_cost = abs(ai - aj) + abs(bi - bj)
                    heapq.heappush(minH, [neighbor_cost, j])
        return res

        