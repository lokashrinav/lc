class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            total = points[i][0] * points[i][0] + points[i][1] * points[i][1]
            heap.append((total, points[i]))
        
        heapq.heapify(heap)

        res = []
        for i in range(k):
            final, points = heapq.heappop(heap)
            res.append(points)
        
        return res

