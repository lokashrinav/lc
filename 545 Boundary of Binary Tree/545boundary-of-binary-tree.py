# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        arr = [root.val]

        if not root.right and not root.left:
            return arr

        def grabLeft(node, left):
            if not node:
                return []
        
            curr = []
            if left:
                curr = [node.val]

            if not node.left and not node.right:
                return []
            elif node.left:
                arr = grabLeft(node.left, True) 
            elif node.right:
                arr = grabLeft(node.right, True)
            
            return curr + arr
                
        arr += grabLeft(root.left, True)
        print(arr)

        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [node.val]
            
            return dfs(node.left) + dfs(node.right)

        arr += dfs(root)
        print(arr)

        def grabRight(node, left):
            if not node:
                return []
        
            curr = []
            if left:
                curr = [node.val]

            if not node.left and not node.right:
                return []
            elif node.right:
                arr = grabRight(node.right, True)
            elif node.left:
                arr = grabRight(node.left, True)
            
            return curr + arr

        arr += grabRight(root.right, True)[::-1]
        print(arr)

        return arr


        