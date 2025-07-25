# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def dfs(node):
            if not node:
                return

            if not node.left and not node.right:
                return
            
            if not node.left:
                res.append(node.right.val)
            
            if not node.right:
                res.append(node.left.val)
            
            dfs(node.left)
            dfs(node.right)
    
        dfs(root)

        return res
        