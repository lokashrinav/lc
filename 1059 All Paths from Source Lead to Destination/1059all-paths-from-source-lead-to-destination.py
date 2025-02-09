class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj = defaultdict(list)
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
        
        visited = set()

        if len(adj[destination]) != 0:
            return False

        cache = {}
        def dfs(num):
            if num in cache:
                return cache[num]

            if num == destination:
                return True
            
            if len(adj[num]) == 0:
                return False

            cache[num] = False
            
            for edge in adj[num]:
                if not dfs(edge):
                    cache[num] = False
                    return cache[num]

            cache[num] = True
            return cache[num]

        return dfs(source)
        
