# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        i, stack = 0, []
        while i < len(s):
            if s[i] == ')':
                stack.pop()
                i += 1
            elif s[i] == '(':
                i += 1
            else:
                signed = False
                num = 0
                while i < len(s) and (s[i].isdigit() or s[i] == '-'):
                    if s[i] == '-': 
                        signed = True
                    else:
                        num = num * 10 + int(s[i])
                    i += 1

                node = TreeNode(-num if signed else num)

                if stack:
                    parent = stack[-1]
                    if not parent.left:
                        parent.left = node
                    else:
                        parent.right = node
                stack.append(node)
        
        return stack[0] if stack else None

                

            
            

            
            



        