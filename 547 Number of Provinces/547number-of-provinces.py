class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        parent = [i for i in range(len(isConnected))]
        rank = [1] * len(isConnected)

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

        for i in range(len(isConnected)):
            for p in range(len(isConnected[0])):
                if isConnected[i][p] == 1:
                    union(i, p)
        
        hset = set()
        for i in range(len(isConnected)):
            smth = find(i)
            hset.add(smth)

        return len(hset) 

        