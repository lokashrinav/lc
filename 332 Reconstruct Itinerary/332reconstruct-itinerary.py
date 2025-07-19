from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets):
        g = defaultdict(list)
        for a, b in tickets:
            heapq.heappush(g[a], b)

        route = []
        def visit(u):
            heap = g[u]
            while heap:
                v = heapq.heappop(heap)  # consume smallest remaining ticket
                visit(v)
            route.append(u)              # post-order
        visit("JFK")
        return route[::-1]
