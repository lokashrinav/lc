class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        hmap = defaultdict(list)
        for first, sec in edges:
            hmap[first].append(sec)
            hmap[sec].append(first)
        
        def dfs(src):
            queue = deque([(src, 1)])
            maxMap = {src:1}
            while queue:
                out, length = queue.popleft()
                for elem in hmap[out]:
                    if elem in maxMap:
                        if maxMap[elem] == length:
                            return (-1, [src])
                        continue
                    queue.append((elem, length + 1))
                    maxMap[elem] = length + 1
            return (max(maxMap.values()), list(maxMap.keys()))
 
        visited = set()

        res = 0
        for i in range(1, n + 1):
            maxNum = 0
            if i in visited:
                continue

            x, comp = dfs(i)
            if x == -1:
                return -1

            for elem in comp:
                x2, comp2 = dfs(elem)
                maxNum = max(x2, maxNum)
                visited.add(elem)

            res += maxNum

        return res
        
