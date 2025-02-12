class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # 0 -> 1, 2
        # 2 -> 5
        # 3 -> 4
        # 4 -> 2

        adj = defaultdict(list)
        for y, x in edges:
            adj[x].append(y)
        
        res = []
        for i in range(n):
            if not adj[i]:
                res.append(i)
        
        return res
