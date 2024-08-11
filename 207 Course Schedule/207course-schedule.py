class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node, hmap):
            if node in visited:
                return False
            if node not in hmap.keys() or hmap[node] == []:
                return True
            visited.add(node)
            for i in range(len(hmap[node])):
                if dfs(hmap[node][i], hmap) == False:
                    return False
            visited.remove(node)
            hmap[node] = []
            return True
        
        hmap = {}
        visited = set()

        for x, y in prerequisites:
            if x not in hmap.keys():
                hmap[x] = []
            hmap[x].append(y)

        for i in hmap.keys():
            if dfs(i, hmap) == False:
                return False
            

        return True
        
            
            



                
        '''while condition:
            slow = prerequisites[slow]

            if slow == fast:
                return False'''
        
        return True
        
        # [1, 0], [1, 2], [2, 0], [3, 2], [3, 1], [5, 7]

        # 0 -> 1
        # 0 -> 2
        # 1 -> 2
        # 1 -> 3
        # 5 -> 7
        # 2 -> 3

        





