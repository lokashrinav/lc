class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        

        adj = defaultdict(list)
        markedSet = set(marked)
        for y, x, val in edges:
            adj[y].append((x, val))
        
        minHeap = [(0, s)]
        distance = {s:0}
        while minHeap:
            val, out = heappop(minHeap)
            if out in markedSet:
                return val
            
            for elem, cost in adj[out]:
                if elem in distance and cost + val < distance[elem]:
                    distance[elem] = cost + val
                    heappush(minHeap, (cost + val, elem))
                elif elem not in distance:
                    distance[elem] = cost + val
                    heappush(minHeap, (cost + val, elem))
        
        return -1



        
