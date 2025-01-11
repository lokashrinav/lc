# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = []
        def dfs(node):
            if not node:
                return
            if node.val == val:
                res.append(node)
            elif val > node.val:
                dfs(node.right)
            else:
                dfs(node.left)            

        dfs(root)
        return res[0] if len(res) >= 1 else None