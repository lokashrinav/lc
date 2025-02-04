# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> None:
#        
#
#    def isTarget(self) -> bool:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        idk = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R':(0, 1)}
        op = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

        visited = set()
        target = [None]
        def dfs(y, x):
            
            visited.add((y, x))

            if master.isTarget():
                target[0] = (y, x)
            
            for key in idk:
                y2, x2 = idk[key]
                ny, nx = y + y2, x + x2
                if (ny, nx) not in visited and master.canMove(key):
                    master.move(key)
                    dfs(ny, nx)
                    master.move(op[key])

        dfs(0, 0)

        if not target[0]:
            return -1
        
        queue = deque([[0, 0, 0]])
        while queue:
            y, x, dist = queue.popleft()
            if (y, x) == target[0]:
                return dist
            
            for key in idk:
                y2, x2 = idk[key]
                ny, nx = y + y2, x + x2
                if (ny, nx) in visited:
                    queue.append([ny, nx, dist + 1])
                    visited.remove((ny, nx))
        
        return -1



        
