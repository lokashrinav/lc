class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for y, x in connections:
            adj[y].append(x)
            adj[x].append(y)

        
        visited = set()

        def dfs(num):
            for elem in adj[num]:
                if elem not in visited:
                    visited.add(elem)
                    dfs(elem)

        
        count = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1
        
        return count - 1 if n <= len(connections) + 1 else -1
