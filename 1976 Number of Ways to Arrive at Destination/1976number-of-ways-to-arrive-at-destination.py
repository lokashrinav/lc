class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for y, x, val in roads:
            adj[y].append((x, val))
            adj[x].append((y, val))
        
        minHeap = [(0, 0)]
        prev = None
        count = 0
        distance = {0:0}
        ways = [0] * n
        ways[0] = 1


        while minHeap:
            # print(minHeap)
            val, out = heappop(minHeap)

            for elem, weight in adj[out]:
                if elem not in distance or (elem in distance and weight + val < distance[elem]):
                    distance[elem] = weight + val
                    ways[elem] = ways[out]
                    heappush(minHeap, (weight + val, elem))
                elif elem in distance and weight + val == distance[elem]:
                    ways[elem] = (ways[elem] + ways[out]) % (10**9 + 7)

        return ways[n - 1]
