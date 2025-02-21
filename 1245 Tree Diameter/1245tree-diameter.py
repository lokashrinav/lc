class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        adj = defaultdict(set)
        for y, x in edges:
            adj[y].add(x)
            adj[x].add(y)

        queue = deque()
        for key in adj:
            if len(adj[key]) == 1:
                queue.append(key)
        
        remaining = len(adj)
        depth = 0
        while remaining > 2:
            remaining -= len(queue)
            for i in range(len(queue)):
                out = queue.popleft()
                for key in adj[out]:
                    adj[key].remove(out)
                    if len(adj[key]) == 1:
                        queue.append(key)
            
            depth += 1

        print(queue)
        return depth * 2 + 1 if len(queue) == 2 else depth * 2

        

