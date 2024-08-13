# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        
        def dfs(node, val):
            print(node, val)

            if node.left:
                result = dfs(node.left, val)
                if result[1] == True:
                    return result
                elif result[0] == k:
                    return (node.val, True)
                val = result[0]
            print(node, val)
            val += 1

            if val == k:
                return (node.val, True)

            if node.right:
                result = dfs(node.right, val)
                if result[1] == True:
                    return result
                elif result[0] == k:
                    return (node.val, True)
                val = result[0]
            return (val, False)

        return dfs(root, 0)[0]
        



        