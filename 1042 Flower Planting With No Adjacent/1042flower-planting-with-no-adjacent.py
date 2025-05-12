class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        idk = defaultdict(list)

        for y, x in paths:
            idk[y - 1].append(x - 1)
            idk[x - 1].append(y - 1)

        hmap = {}

        for i in range(n):
            hmap[i] = [1, 2, 3, 4]
        
        hmap2 = {}
        
        visited = set()

        def dfs(i):
            if i in visited:
                return
            
            hmap2[i] = hmap[i][0]

            visited.add(i)

            for elem in idk[i]:
                if hmap2[i] in hmap[elem]:
                    hmap[elem].remove(hmap2[i])
            
            for elem in idk[i]:
                dfs(elem)

        for i in range(n):
            if i not in visited:
                dfs(i)
        
        
        res = []

        for i in range(n):
            res.append(hmap2[i])
        
        return res
        

        
