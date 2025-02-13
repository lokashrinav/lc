# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        final = [None]

        flag = [False]

        def dfs(node):
            if not node:
                return False

            if p.val < node.val:
                dfs(node.left)

            if flag[0]:
                final[0] = node
                flag[0] = False
                return False

            if node.val == p.val:
                flag[0] = True
            
            if node.val < p.val or flag[0]:
                dfs(node.right)

        dfs(root)

        return final[0]

