# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def printTree(node):
            if not node:
                return
            print(node.val, end=" ")
            printTree(node.left)
            printTree(node.right)
        
        def dfs(node, prev, dire):
            nonlocal root
            if not node:
                return
                                
            if node.val > high:
                node.right = None
                if prev is None:
                    root = node.left
                    dfs(root, None, None)
                    return
                if dire:
                    prev.left = node.left
                    dfs(node.left, prev, True)
                else:
                    prev.right = node.left
                    dfs(node.left, prev, False)
            elif node.val < low:
                node.left = None
                if prev is None:
                    root = node.right
                    dfs(root, None, None)
                    return
                if dire:
                    prev.left = node.right
                    dfs(node.right, prev, True)
                else:
                    prev.right = node.right
                    dfs(node.right, prev, False)
            else:
                dfs(node.left, node, True)
                dfs(node.right, node, False)

        dfs(root, None, None)

        return root