# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return False
            
            if not node.left and not node.right and node.val == target:
                return True
            
            first = dfs(node.left)
            second = dfs(node.right)

            if first:
                node.left = None

            if second:
                node.right = None
            
            if not node.left and not node.right and node.val == target:
                return True

            return False

        if dfs(root):
            return None
        
        return root
        