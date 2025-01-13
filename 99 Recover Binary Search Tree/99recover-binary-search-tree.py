# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        res = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            res.append(node)
            inorder(node.right)
        
        inorder(root)

        first, second = None, None
        print([res1.val for res1 in res])
        for i in range(len(res) - 1):
            if res[i].val > res[i + 1].val:
                if not first:
                    first = res[i]
                second = res[i + 1]
        
        if first and second:
            first.val, second.val = second.val, first.val

        return root 
            