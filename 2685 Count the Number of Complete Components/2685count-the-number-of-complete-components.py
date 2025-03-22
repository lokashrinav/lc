class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for y, x in edges:
            adj[y].append(x)
            adj[x].append(y)
        
        visited = set()

        def dfs(num):
            if num in visited:
                return

            visited.add(num)
            for num2 in adj[num]:
                dfs(num2)
        
        def check(visited):
            for elem in visited:
                if len(adj[elem]) != len(visited) - 1:
                    return False
            return True
                
            
        count = 0
        prev = set()
        for i in range(n):
            visited = set()
            if i in prev:
                continue
            dfs(i)
            prev.update(visited)
            if check(visited):
                count += 1
        
        return count
