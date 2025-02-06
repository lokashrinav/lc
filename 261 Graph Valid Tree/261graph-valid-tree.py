class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges and n > 1:
            return False
        
        parent = {i:i for i in range(n)}

        rank = [1 for i in range(n)]

        def union(p1, p2):
            anc1 = find(p1)
            anc2 = find(p2)
            if anc1 == anc2:
                return False
            
            if rank[anc1] >= rank[anc2]:
                rank[anc1] += rank[anc2]
                parent[anc2] = anc1
            else:
                rank[anc2] += rank[anc1]
                parent[anc1] = anc2
            return True

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
                
        for i in range(len(edges)):
            if not union(edges[i][1], edges[i][0]):
                return False
        
        print(parent)
        
        if rank[find(0)] != n:
            return False

        print('d')
        
        print(rank)
        print(parent)
        
        return True
        


        