# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dummy = head = TreeNode()
        def dfs(preorder, inorder):
            if len(preorder) == 0:
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            tree = TreeNode(preorder[0])
            saved = inorder.index(preorder[0])
            tree.left = dfs(preorder[1: 1 + saved], inorder[:saved])
            tree.right = dfs(preorder[1 + saved:], inorder[saved + 1:])
            return tree

        dummy.left = dfs(preorder, inorder)
        return head.left

        
        