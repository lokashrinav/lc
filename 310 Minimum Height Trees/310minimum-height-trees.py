class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(set)
        for y, x in edges:
            adj[y].add(x)
            adj[x].add(y)

        queue = deque()
        for i in range(n):
            if len(adj[i]) == 1:
                queue.append(i)

        remaining = n

        depth = 0
        while remaining > 2:
            remaining -= len(queue)
            depth += 1
            for i in range(len(queue)):
                out = queue.popleft()

                for nei in adj[out]:
                    adj[nei].remove(out)
                    if len(adj[nei]) == 1:
                        queue.append(nei)
        
        return list(queue)
