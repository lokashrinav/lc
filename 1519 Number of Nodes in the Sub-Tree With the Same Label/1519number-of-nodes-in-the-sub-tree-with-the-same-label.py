class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        paths = defaultdict(list)
        for y, x in edges:
            paths[y].append(x)
            paths[x].append(y)

        visited = set()
        hmap = {}
        def dfs(num):
            new = [0] * 26
            if num in visited:
                return new
            visited.add(num)
            new[ord(labels[num]) - 97] += 1
            for elem in paths[num]:
                re = dfs(elem)
                for i in range(26):
                    new[i] += re[i]
            hmap[num] = new[ord(labels[num]) - 97]
            return new

        dfs(0)
        res = [0] * n
        print(hmap)
        for i in range(n):
            res[i] = hmap[i]
        
        return res
        