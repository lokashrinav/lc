class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(curr, end, prod):
            if curr == end:
                return prod
            
            minNum = -1
            for num in graph[curr]:
                if num not in visited:
                    visited.add(num)
                    minNum = max(minNum, dfs(num, end, prod * graph[curr][num]))
                    if minNum != -1:
                        return minNum
            
            return minNum


        graph = defaultdict(dict)

        for i, (num, dem) in enumerate(equations):
            graph[num][dem] = values[i]
            graph[dem][num] = 1 / values[i]
        
        res = []
        for num, dem in queries:
            if num not in graph or dem not in graph:
                res.append(float(-1))
            elif num == dem:
                res.append(float(1))
            else:
                visited = set()
                res.append(dfs(num, dem, 1))
        
        return res

        