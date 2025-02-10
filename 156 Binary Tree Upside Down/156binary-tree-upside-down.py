# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        
        left = [None]

        def dfs(curr, prev, right):
            if not curr:
                return
            
            dfs(curr.left, curr, curr.right)

            if not curr.left and left[0] == None: 
                left[0] = curr
            
            curr.right = prev
            curr.left = right

        dfs(root, None, None)

        return left[0]
        