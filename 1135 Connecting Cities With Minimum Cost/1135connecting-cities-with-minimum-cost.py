class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for y, x, cost in connections:
            adj[y].append((x, cost))
            adj[x].append((y, cost))
        
        heap = [(0, 1)]
        visited = set()
        total = 0

        while heap and len(visited) < n:
            cost, city = heappop(heap)
            if city in visited:
                continue
            
            total += cost
            visited.add(city)

            for u, cost in adj[city]:
                if u not in visited:
                    heappush(heap, (cost, u))
        
        return total if n == len(visited) else -1
        
        
