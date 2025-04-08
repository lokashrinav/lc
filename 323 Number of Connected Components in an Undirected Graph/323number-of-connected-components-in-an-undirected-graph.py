class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        parent = {i:i for i in range(n)}
        rank = [1] * n 

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(p1, p2):
            idk1 = find(p1)
            idk2 = find(p2)
            
            if idk1 != idk2:
                if rank[idk1] >= rank[idk2]:
                    rank[idk1] += rank[idk2]
                    parent[idk2] = idk1
                else:
                    rank[idk2] += rank[idk1]
                    parent[idk1] = idk2

        for i in range(len(edges)):
            union(edges[i][0], edges[i][1])

        hset = set()
        total = 0

        # print(parent)
        for i in range(n):
            idk1 = find(i)
            hset.add(idk1)

        return len(hset)


        



        