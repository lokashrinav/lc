class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        adj = defaultdict(list)

        for y, x in roads:
            adj[y].append(x)
            adj[x].append(y)

        for i in range(n):
            if i in adj:
                adj[i] = set(adj[i])
        
        maxNum = 0
        for i in range(n):
            for p in range(i + 1, n):
                carry = 1 if i in adj[p] else 0
                maxNum = max(maxNum, len(adj[i]) + len(adj[p]) - carry)
        
        return maxNum


