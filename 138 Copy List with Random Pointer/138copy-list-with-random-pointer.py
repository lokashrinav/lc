"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hmap = {}

        def dfs(node):
            if not node:
                return None

            newNode = Node(node.val)
            hmap[node] = newNode

            if node.next in hmap:
                newNode.next = hmap[node.next]
            else:
                newNode.next = dfs(node.next)
            
            if node.random in hmap:
                newNode.random = hmap[node.random]
            else:
                newNode.random = dfs(node.random)
            
            return newNode
        
        return dfs(head)
        