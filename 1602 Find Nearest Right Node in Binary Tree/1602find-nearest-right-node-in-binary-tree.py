# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:

        queue = deque([root])

        flag = False
        solved = None

        while queue:
            for i in range(len(queue)):
                out = queue.popleft()
                if flag:
                    solved = out
                    flag = False
                if out == u:
                    flag = True

                if out.left:
                    queue.append(out.left)
                if out.right:
                    queue.append(out.right)
            
            if flag and not solved:
                return None
            
            if solved:
                return solved
        
        return None

                
            
