# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        visited = {}

        def dfs(node):
            if not node:
                return None
            
            if node in visited:
                return visited[node]

            newNode = NodeCopy()

            visited[node] = newNode
            
            newNode.val = node.val
            newNode.left = dfs(node.left)
            newNode.right = dfs(node.right)
            newNode.random = dfs(node.random)
            
            return newNode

        return dfs(root)