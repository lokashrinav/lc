class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        visited = set()
        adj = defaultdict(list)

        for i in range(len(ppid)):
            adj[ppid[i]].append(pid[i])

        def dfs(num):
            for q in adj[num]:
                if q not in visited:
                    visited.add(q)
                    dfs(q)

        visited.add(kill)
        dfs(kill)

        return list(visited)
            
