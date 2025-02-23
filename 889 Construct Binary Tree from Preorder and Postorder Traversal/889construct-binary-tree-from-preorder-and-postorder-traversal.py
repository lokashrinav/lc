# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        convert = {}
        for i, n in enumerate(postorder):
            convert[n] = i
        
        def dfs(i1, i2, j1, j2):
            if i2 < i1:
                return None

            root = TreeNode(preorder[i1])
            if i1 != i2:
                find = convert[preorder[i1 + 1]]
                root.left = dfs(i1 + 1, (find - j1 + 1) + i1, j1, find)
                root.right = dfs(i1 + (find - j1) + 2, i2, find + 1, j2 - 1)

            return root
        
        return dfs(0, len(preorder) - 1, 0, len(preorder) - 1)