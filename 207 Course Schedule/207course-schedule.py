class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        paths = defaultdict(list)
        for y, x in prerequisites:
            paths[x].append(y)
        
        visited = set()
        curr = set()

        '''
        0 -> 1
        0 -> 2
        1 -> 3
        2 -> 3

        '''

        def dfs(num):
            if num in curr:
                return True
            if num in visited:
                return False

            curr.add(num)
            visited.add(num)

            for elem in paths[num]:
                if dfs(elem):
                    return True
            
            curr.remove(num)
            
            return False  

        '''

        4 -> 1
        4 -> 2
        3 -> 1
        3 -> 2

        '''      

        for i in range(numCourses):
            curr = set()
            if dfs(i):
                return False
        
        return True

        
