from typing import Optional

class Solution:
    def isSubPath(self, head: Optional['ListNode'], root: Optional['TreeNode']) -> bool:
        def check(node, node2):
            if not node2:
                return True
            elif not node:
                return False
            elif not node or not node2:
                return False
            elif node.val != node2.val:
                return False
            else:
                return check(node.right, node2.next) or check(node.left, node2.next)

        def dfs(node):
            if not node:
                return False
            if check(node, head):
                return True
            else:
                return dfs(node.left) or dfs(node.right)

        return dfs(root)


        
