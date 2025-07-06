class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        hmap = defaultdict(int)
        paths = defaultdict(list)
        idk = defaultdict(int)

        for y, x in connections:
            paths[y].append(x)
            paths[x].append(y)

        visited = {}
        final = []
        final.append([])
        
        def dfs(curr):
            final[-1].append(curr)
            for elem in paths[curr]:
                if elem not in visited:
                    visited[elem] = len(final) - 1
                    dfs(elem)
            
        for i in range(1, c + 1):
            if i not in visited:
                visited[i] = len(final) - 1
                dfs(i)
                heapify(final[-1])
                final.append([])
            
        res = []

        for y, x in queries:
            if y == 1:
                if x not in hmap or hmap[x] == 0:
                    res.append(x)
                else:
                    res.append(final[visited[x]][0] if final[visited[x]] else -1)
                    
            elif y == 2:
                hmap[x] = 1
                while final[visited[x]] and hmap[final[visited[x]][0]] == 1:
                    heappop(final[visited[x]])

        return res
        
        