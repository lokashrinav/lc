class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visited = set()
        final = set()
        unsafe = set()

        def dfs(num):
            if num in unsafe:
                return False

            if num in final:
                return True

            if len(graph[num]) == 0:
                return True
            
            if num in visited:
                return False
            
            visited.add(num)

            for i in range(len(graph[num])):
                if not dfs(graph[num][i]):
                    visited.remove(num)
                    unsafe.add(num)
                    return False
            
            visited.remove(num)
            final.add(num)
            return True
        
        res = []

        for i in range(len(graph)):
            first = dfs(i)
            if first:
                res.append(i)
                final.add(i)
        
        return res
        