class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minHeap = []
        i = 0
        res = {}
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while minHeap and q > minHeap[0][1]:
                heapq.heappop(minHeap)
            if minHeap:
                x, y = minHeap[0]
                res[q] = x
            else:
                res[q] = -1
        return [res[i] for i in queries]



            


        
