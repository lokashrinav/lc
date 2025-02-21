class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        adj = defaultdict(list)

        def dfs(src, end, visited):
            if src == end:
                return True

            if src not in adj or src in visited:
                return False

            visited.add(src)
            
            for nei in adj[src]:
                if nei not in visited:
                    if dfs(nei, end, visited):
                        return True
            
            return False

        for s in equations:
            if s[1] == "=":
                adj[s[0]].append(s[3])
                adj[s[3]].append(s[0])
        
        for s in equations:
            if s[1] == "!":
                if dfs(s[0], s[3], set()):
                    return False
        
        return True
                
        

