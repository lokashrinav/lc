# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, level):
            if not node:
                return (level, None)
            
            left, idk1, = dfs(node.left, level + 1)
            right, idk2 = dfs(node.right, level + 1)

            #print(node.val, left, right)

            if left == right:
                return (left, node)
            elif right > left:
                return (right, idk2)
            else:
                return (left, idk1)

        idk1, idk2 = dfs(root, 0)

        return idk2
        
        
        