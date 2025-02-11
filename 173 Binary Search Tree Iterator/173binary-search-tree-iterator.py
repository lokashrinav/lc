# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.dfs(root)
        self.stack.reverse()
        
    def next(self) -> int:
        return self.stack.pop()
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0
    
    def dfs(self, node):
        if not node:
            return
        
        self.dfs(node.left)
        self.stack.append(node.val)
        self.dfs(node.right)

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()