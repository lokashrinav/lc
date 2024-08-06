class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            p1 = -heapq.heappop(max_heap)
            p2 = -heapq.heappop(max_heap)
            if p1 == p2:
                continue
            elif p1 < p2:
                heapq.heappush(max_heap, -(p2 - p1))
            else:
                heapq.heappush(max_heap, -(p1 - p2))

        return -max_heap[0] if max_heap else 0


        