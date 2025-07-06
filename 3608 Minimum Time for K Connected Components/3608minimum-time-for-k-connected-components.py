class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:

        edges.sort(key=lambda x: (x[2], -x[1], -x[0]))
               
        def dfs(num, paths):
            for elem in paths[num]:
                if elem not in visited:
                    visited.add(elem)
                    dfs(elem, paths)

        paths = defaultdict(list)
        for i in range(len(edges)):
            y, x, time = edges[i]
            paths[y].append(x)
            paths[x].append(y)

        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i, paths)

        if count == k:
            return 0

        l, r = 0, len(edges) - 1
        saved = float('inf')

        while l <= r:
            m = (l + r) // 2
            paths = defaultdict(list)
            for i in range(m + 1, len(edges)):
                y, x, time = edges[i]
                paths[y].append(x)
                paths[x].append(y)

            count = 0
            visited = set()
            for i in range(n):
                if i not in visited:
                    count += 1
                    visited.add(i)
                    dfs(i, paths)

            #print(paths, count, m)
            
            if count > k:
                r = m - 1
            elif count < k:
                l = m + 1
            else:
                saved = min(saved, edges[m][2])
                r = m - 1
                
        return saved if saved != float('inf') else 0
            
            
            
        