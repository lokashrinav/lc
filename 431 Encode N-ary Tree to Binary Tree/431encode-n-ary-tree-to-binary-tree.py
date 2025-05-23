"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:

        def printNode(node):
            if not node:
                return
                
            queue = deque([(node, None)])
            while queue:
                for i in range(len(queue)):
                    out, left = queue.popleft()
                    print(out.val, left, end=" ")

                    if out.left:
                        queue.append((out.left, "left"))
                    if out.right:
                        queue.append((out.right, "right"))
                print("")

        if not root:
            return None

        head = None
        def dfs(node):
            nonlocal head

            curr = first = TreeNode(node.val)
            if not head:
                head = curr
            
            flag = False
            for elem in node.children:
                if not flag:
                    curr.left = dfs(elem)
                    curr = curr.left
                else:
                    curr.right = dfs(elem)
                    curr = curr.right
                flag = True
            
            return first
        
        dfs(root) 

        return head 

        #printNode(head)  
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        
        head = None
        def dfs(node):

            nonlocal head

            if not node:
                return None
            
            calc = first = Node(node.val)
            if not head:
                head = calc
            
            node = node.left
            calc.children = []
            while node:
                calc.children.append(dfs(node))
                node = node.right
        
            return first

        dfs(data)

        return head
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))