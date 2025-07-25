# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        list1 = []
        list2 = []
        def dfs(node, l):
            if not node:
                return
            
            if not node.left and not node.right:
                l.append(node.val)
            
            dfs(node.left, l)
            dfs(node.right, l)
        
        dfs(root1, list1)
        dfs(root2, list2)

        return list1 == list2


        