# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node):
            if not node:
                return []

            str1 = str(node.val)

            newStr = []
            left = dfs(node.left)
            right = dfs(node.right)
            if not left and not right:
                newStr.append(str1)

            for elem in left:
                newStr.append(str1 + "->" + elem)
            for elem in right:
                newStr.append(str1 + "->" + elem)

            return newStr
        
        return dfs(root)
        