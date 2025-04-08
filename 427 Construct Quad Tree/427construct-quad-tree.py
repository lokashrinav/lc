"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(y1, x1, y2, x2):
            num = None
            flag = True
            for y in range(y1, y2):
                for x in range(x1, x2):
                    if num is None:
                        num = grid[y][x]
                    elif num != grid[y][x]:
                        flag = False

            if flag:
                newNode = Node(num, True, None, None, None, None)
            else:
                y_mid = (y1 + y2) // 2
                x_mid = (x1 + x2) // 2
                topLeft = dfs(y1, x1, y_mid, x_mid)
                topRight = dfs(y1, x_mid, y_mid, x2)
                bottomLeft = dfs(y_mid, x1, y2, x_mid)
                bottomRight = dfs(y_mid, x_mid, y2, x2)
                newNode = Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

            return newNode
        
        return dfs(0, 0, len(grid), len(grid[0]))

        