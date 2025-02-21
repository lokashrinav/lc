# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.hset = set()
        def dfs(node, curr):
            if not node:
                return
                
            self.hset.add(curr)
            
            if node.right:
                dfs(node.right, 2 * curr + 2)

            if node.left:
                dfs(node.left, 2 * curr + 1)

        dfs(root, 0)
        

    def find(self, target: int) -> bool:
        return target in self.hset

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)