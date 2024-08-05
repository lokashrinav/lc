# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not subRoot:
                return True
            if not root:
                return False
            
            if self.check(root, subRoot) == True:
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def check(self, node, node2):
        if not node and not node2:
            return True
        if node and node2 and node2.val == node.val:
            return self.check(node.left, node2.left) and self.check(node.right, node2.right)
        return False
        