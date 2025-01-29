class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(p1):
            while p1 != par[p1]:
                p1 = par[p1]
            return p1
        
        def union(p1, p2):
            s_p1, s_p2 = p1, p2
            p1, p2 = find(p1), find(p2)

            if p1 == p2:
                return (s_p1, s_p2)
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return None

        count = 0
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        for a, b in edges:
            x = union(a, b)
            if x:
                return x
        return 
        