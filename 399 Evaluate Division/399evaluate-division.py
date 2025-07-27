class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        paths = defaultdict(list)
        ind = 0

        for y, x in equations:
            paths[y].append((x, False, values[ind]))
            paths[x].append((y, True, values[ind]))
            ind += 1
        
        def dfs(y, x):
            if y == x:
                return 1
            if y in visited:
                return -1

            visited.add(y)

            for elem, idk, fun in paths[y]:
                calc = dfs(elem, x) 
                if calc != -1:
                    if not idk:
                        return fun * calc
                    else:
                        return calc / fun
            
            return -1

        res = []
        for y, x in queries:
            visited = set()
            if y not in paths or x not in paths:
                res.append(-1)
                continue

            res.append(dfs(y, x))
    
        return res
