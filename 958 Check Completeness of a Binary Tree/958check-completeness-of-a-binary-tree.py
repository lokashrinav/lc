# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])

        while queue:
            length = len(queue)
            for i in range(len(queue)):
                out = queue.popleft()
                if out is not None:
                    queue.append(out.left)
                    queue.append(out.right)
                else:
                    while queue:
                        out2 = queue.popleft()
                        if out2:
                            return False   
                    return True                  

        return True
        