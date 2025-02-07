class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []
        visited = set()

        def dfs(num, curr):

            if num == len(graph) - 1:
                res.append(curr.copy())
                return
            
            for i in range(len(graph[num])):
                curr.append(graph[num][i])
                dfs(graph[num][i], curr)
                curr.pop()

        dfs(0, [0])

        return res