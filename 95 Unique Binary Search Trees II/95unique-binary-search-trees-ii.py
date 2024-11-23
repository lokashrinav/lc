# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left, right):
            if left > right:
                return [None]
            res = []
            for i in range(left, right + 1):
                for p in generate(left, i - 1):
                    for j in generate(i + 1, right):
                        node = TreeNode(i, p, j)
                        res.append(node)
            return res
    
        return generate(1, n)
        