class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for y, x in dislikes:
            adj[y].append(x)
            adj[x].append(y)

        seen = set()

        def dfs(num, count):
            if num in visited and (count - visited[num]) % 2:
                return False
            
            if num in seen:
                return True

            visited[num] = count

            seen.add(num)

            for y in adj[num]:
                if not dfs(y, count + 1):
                    return False
            
            return True
        
        for i in range(n):
            visited = defaultdict(int)
            if not dfs(i, 0):
                return False
        
        return True
        
