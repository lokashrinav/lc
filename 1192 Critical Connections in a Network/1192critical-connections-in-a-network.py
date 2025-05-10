class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        hmap = defaultdict(list)

        res = []

        for y, x in connections:
            hmap[y].append(x)
            hmap[x].append(y)

        time = 0
        low = [-1] * n
        disc = [-1] * n

        def dfs(node, parent):
            nonlocal time
            low[node] = disc[node] = time
            time += 1
            for v in hmap[node]:
                if v == parent:
                    continue
                if disc[v] == -1:
                    dfs(v, node)
                    low[node] = min(low[node], low[v])
                    if low[v] > disc[node]:
                        res.append([node, v])
                else:
                    low[node] = min(low[node], disc[v])

        dfs(0, -1)
        return res


        
