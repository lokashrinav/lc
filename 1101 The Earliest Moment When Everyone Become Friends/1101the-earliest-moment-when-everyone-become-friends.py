class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

        logs.sort()
        rank = [1] * n
        parent= [i for i in range(n)]

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
                
        def union(a, b):
            first = find(a)
            second = find(b)

            if first == second:
                return 0

            if rank[first] >= rank[second]:
                rank[first] += rank[second]
                parent[second] = first
                return rank[first]
            else:
                rank[second] += rank[first]
                parent[first] = second
                return rank[second]

        for i in range(len(logs)):
            out = union(logs[i][1], logs[i][2])

            print(rank, parent)

            if out == n:
                return logs[i][0]
        
        return -1
        