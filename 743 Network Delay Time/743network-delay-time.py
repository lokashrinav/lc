class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for src, dst, weight in times:
            adj[src].append([dst, weight])

        arr = [None for i in range(n)]

        minHeap = [[0, k]]
        shortest = {}

        count = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 in shortest:
                    continue
                heapq.heappush(minHeap, [w1 + w2, n2])

        if len(shortest) != n:
            return -1

        return max(shortest.values())

        

        

        
        