class Solution:
    def isPathCrossing(self, path: str) -> bool:

        curr = [0, 0]
        visited = set()

        hmap = {"N": (1, 0), "S": (-1, 0), "W": (0, 1), "E": (0, -1)}

        def dfs(curr, ind):
            print(curr, visited)

            if tuple(curr) in visited:
                return False

            if ind == len(path):
                return True
            
            visited.add(tuple(curr))
            
            curr[0] += hmap[path[ind]][0]
            curr[1] += hmap[path[ind]][1]
            
            return dfs(curr, ind + 1)

        return not dfs(curr, 0)
        